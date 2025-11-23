# Sistema de Inventario de Equipos de Red
# Implementación en Python utilizando POO, MySQL y Tkinter

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
import csv
import datetime

# -------------------------
# CONFIGURACIÓN BASE DE DATOS
# -------------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "sistema_inventario"
}

# -------------------------
# FUNCIONES DE BASE DE DATOS
# -------------------------
def obtener_conexion():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        messagebox.showerror("DB Error", f"No se pudo conectar a la base de datos:\n{e}")
        return None

def crear_tabla_si_no_existe():
    conn = obtener_conexion()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipos (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nombre VARCHAR(100) NOT NULL,
      ip VARCHAR(45) NOT NULL,
      tipo VARCHAR(50),
      ubicacion VARCHAR(100),
      estado VARCHAR(20) DEFAULT 'desconocido',
      fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()

# -------------------------
# CLASES (POO)
# -------------------------
class Equipo:
    def __init__(self, nombre, ip, tipo, ubicacion, estado="desconocido"):
        self.nombre = nombre
        self.ip = ip
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.estado = estado

    def to_tuple(self):
        return (self.nombre, self.ip, self.tipo, self.ubicacion, self.estado)

# -------------------------
# FUNCIONES REQUERIDAS
# -------------------------
def RegistrarEquipo(equipo: Equipo):
    """Guarda el equipo en la base de datos."""
    conn = obtener_conexion()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO equipos (nombre, ip, tipo, ubicacion, estado) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, equipo.to_tuple())
        conn.commit()
        return True
    except Error as e:
        messagebox.showerror("Error SQL", str(e))
        return False
    finally:
        cursor.close()
        conn.close()

def MostrarInventario(filtro_ip=None):
    """Devuelve lista de equipos (como diccionarios)."""
    conn = obtener_conexion()
    if conn is None:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        if filtro_ip:
            cursor.execute("SELECT * FROM equipos WHERE ip = %s", (filtro_ip,))
        else:
            cursor.execute("SELECT * FROM equipos ORDER BY id")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        messagebox.showerror("Error SQL", str(e))
        return []
    finally:
        cursor.close()
        conn.close()

def GenerarAlertas():
    """
    Genera alertas: devuelve lista de equipos con estado != 'online'.
    (Se puede extender a ping real; por ahora usamos el campo estado).
    """
    inventario = MostrarInventario()
    alertas = []
    for r in inventario:
        if r.get("estado", "").lower() != "online":
            alertas.append(r)
    return alertas

# -------------------------
# UTILIDADES (vectores/matrices requeridas)
# -------------------------
def construir_vectores_y_matrices():
    """
    Ejemplo simple de creación de:
    - vectores: lista de nombres de equipos y ubicaciones
    - matrices: matriz simple de ips y estados (lista de listas)
    """
    inv = MostrarInventario()
    equipos = [r['nombre'] for r in inv]
    ubicaciones = list({r['ubicacion'] for r in inv})
    # matriz IPs x estados (cada fila: [ip, estado])
    matriz_ips = [[r['ip'], r['estado']] for r in inv]
    return equipos, ubicaciones, matriz_ips

# -------------------------
# INTERFAZ GRÁFICA (tkinter)
# -------------------------
class AppInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Inventario de Equipos de Red")
        self.root.geometry("900x600")
        self.create_widgets()
        crear_tabla_si_no_existe()
        self.refrescar_tabla()

    def create_widgets(self):
        frame_form = tk.LabelFrame(self.root, text="Registrar Equipo", padx=8, pady=8)
        frame_form.place(x=10, y=10, width=420, height=230)

        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.grid(row=0, column=1, pady=4)

        tk.Label(frame_form, text="IP:").grid(row=1, column=0, sticky="w")
        self.entry_ip = tk.Entry(frame_form, width=30)
        self.entry_ip.grid(row=1, column=1, pady=4)

        tk.Label(frame_form, text="Tipo:").grid(row=2, column=0, sticky="w")
        self.entry_tipo = tk.Entry(frame_form, width=30)
        self.entry_tipo.grid(row=2, column=1, pady=4)

        tk.Label(frame_form, text="Ubicación:").grid(row=3, column=0, sticky="w")
        self.entry_ubic = tk.Entry(frame_form, width=30)
        self.entry_ubic.grid(row=3, column=1, pady=4)

        tk.Label(frame_form, text="Estado:").grid(row=4, column=0, sticky="w")
        self.combo_estado = ttk.Combobox(frame_form, values=["online", "offline", "mantenimiento", "desconocido"], state="readonly")
        self.combo_estado.grid(row=4, column=1, pady=4)
        self.combo_estado.set("desconocido")

        btn_registrar = tk.Button(frame_form, text="Registrar Equipo", command=self.registrar_equipo_gui)
        btn_registrar.grid(row=5, column=0, columnspan=2, pady=8)

        # Frame para tabla / consultas
        frame_tabla = tk.LabelFrame(self.root, text="Inventario", padx=8, pady=8)
        frame_tabla.place(x=10, y=250, width=880, height=330)

        columns = ("id", "nombre", "ip", "tipo", "ubicacion", "estado", "fecha")
        self.tree = ttk.Treeview(frame_tabla, columns=columns, show="headings", height=12)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120 if col!="nombre" else 160)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # botones de acciones
        frame_actions = tk.Frame(self.root)
        frame_actions.place(x=440, y=20, width=450, height=200)

        tk.Label(frame_actions, text="Buscar por IP:").pack(anchor="w")
        self.search_ip = tk.Entry(frame_actions)
        self.search_ip.pack(fill="x", pady=4)
        tk.Button(frame_actions, text="Buscar", command=self.buscar_por_ip).pack(fill="x")

        tk.Button(frame_actions, text="Mostrar todo", command=self.refrescar_tabla).pack(fill="x", pady=4)

        tk.Button(frame_actions, text="Generar Alertas", command=self.mostrar_alertas).pack(fill="x", pady=4)
        tk.Button(frame_actions, text="Exportar CSV", command=self.exportar_csv).pack(fill="x", pady=4)
        tk.Button(frame_actions, text="Refrescar (vectores/matrices)", command=self.mostrar_vectores_y_matriz).pack(fill="x", pady=4)

    # -------------------------
    # MÉTODOS GUI
    # -------------------------
    def registrar_equipo_gui(self):
        nombre = self.entry_nombre.get().strip()
        ip = self.entry_ip.get().strip()
        tipo = self.entry_tipo.get().strip()
        ubic = self.entry_ubic.get().strip()
        estado = self.combo_estado.get().strip()

        # Validaciones básicas
        if not nombre or not ip:
            messagebox.showwarning("Validación", "Nombre e IP son obligatorios.")
            return
        # validación simple de IP (formato)
        partes = ip.split('.')
        if len(partes) != 4 or not all(p.isdigit() and 0 <= int(p) <= 255 for p in partes):
            messagebox.showwarning("Validación", "IP inválida. Ejemplo válido: 192.168.1.10")
            return

        equipo = Equipo(nombre, ip, tipo, ubic, estado)
        ok = RegistrarEquipo(equipo)
        if ok:
            messagebox.showinfo("Registro", "Equipo registrado correctamente.")
            self.limpiar_campos()
            self.refrescar_tabla()

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_ip.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_ubic.delete(0, tk.END)
        self.combo_estado.set("desconocido")

    def refrescar_tabla(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        rows = MostrarInventario()
        for r in rows:
            self.tree.insert("", tk.END, values=(r['id'], r['nombre'], r['ip'], r['tipo'], r['ubicacion'], r['estado'], r['fecha_registro']))

    def buscar_por_ip(self):
        ip = self.search_ip.get().strip()
        if not ip:
            messagebox.showwarning("Buscar", "Ingresa una IP para buscar.")
            return
        rows = MostrarInventario(filtro_ip=ip)
        for i in self.tree.get_children():
            self.tree.delete(i)
        for r in rows:
            self.tree.insert("", tk.END, values=(r['id'], r['nombre'], r['ip'], r['tipo'], r['ubicacion'], r['estado'], r['fecha_registro']))

    def mostrar_alertas(self):
        alertas = GenerarAlertas()
        if not alertas:
            messagebox.showinfo("Alertas", "No hay alertas. Todos los equipos están 'online'.")
            return
        text = "Equipos con alerta (estado != 'online'):\n\n"
        for a in alertas:
            text += f"ID:{a['id']} - {a['nombre']} - IP:{a['ip']} - Estado:{a['estado']} - Ubic:{a['ubicacion']}\n"
        messagebox.showwarning("Alertas", text)

    def exportar_csv(self):
        rows = MostrarInventario()
        if not rows:
            messagebox.showinfo("Exportar", "No hay datos para exportar.")
            return
        nombre_arch = f"inventario_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(nombre_arch, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id","nombre","ip","tipo","ubicacion","estado","fecha_registro"])
            for r in rows:
                writer.writerow([r['id'], r['nombre'], r['ip'], r['tipo'], r['ubicacion'], r['estado'], r['fecha_registro']])
        messagebox.showinfo("Exportar", f"Exportado a {nombre_arch}")

    def mostrar_vectores_y_matriz(self):
        equipos, ubicaciones, matriz_ips = construir_vectores_y_matrices()
        info = f"Vectores:\n- Equipos ({len(equipos)}): {equipos}\n- Ubicaciones ({len(ubicaciones)}): {ubicaciones}\n\nMatriz IPs (ip, estado):\n"
        for fila in matriz_ips:
            info += f"{fila}\n"
        messagebox.showinfo("Vectores y Matriz", info)

# -------------------------
# EJECUCIÓN
# -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AppInventario(root)
    root.mainloop()


