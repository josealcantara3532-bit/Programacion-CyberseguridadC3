"""
Sistema de Inventario de Equipos de Red
Incluye:
- Registrar / Editar / Eliminar / Buscar
- Alertas
- Exportar CSV
- Vectores y Matriz
- IP duplicada
- Tabla automática
"""

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
import csv
import datetime


# =============================================================================
# CONFIGURACIÓN DE BASE DE DATOS
# =============================================================================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",            
    "password": "",        
    "database": "sistema_inventario"  
}


# =============================================================================
# CONEXIÓN Y CREACIÓN DE TABLA
# =============================================================================
def obtener_conexion():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except:
        messagebox.showerror("Error", "No se pudo conectar a MySQL.")
        return None


def crear_tabla():
    """Crea la tabla si no existe (se ejecuta automáticamente al iniciar)."""
    conn = obtener_conexion()
    if conn is None:
        return

    try:
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
        )
        """)
        conn.commit()
    except Error as e:
        messagebox.showerror("SQL Error", str(e))
    finally:
        cursor.close()
        conn.close()


# =============================================================================
# CLASE EQUIPO (POO)
# =============================================================================
class Equipo:
    def __init__(self, nombre, ip, tipo, ubicacion, estado="desconocido"):
        self.nombre = nombre
        self.ip = ip
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.estado = estado

    def to_tuple(self):
        return (self.nombre, self.ip, self.tipo, self.ubicacion, self.estado)


# =============================================================================
# CRUD – OPERACIONES SQL
# =============================================================================
def RegistrarEquipo(e):
    conn = obtener_conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO equipos (nombre, ip, tipo, ubicacion, estado) VALUES (%s,%s,%s,%s,%s)",
            e.to_tuple()
        )
        conn.commit()
        return True

    except Error as e:
        messagebox.showerror("SQL", str(e))
        return False

    finally:
        cursor.close()
        conn.close()


def MostrarInventario(filtro_ip=None):
    conn = obtener_conexion()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        if filtro_ip:
            cursor.execute("SELECT * FROM equipos WHERE ip=%s", (filtro_ip,))
        else:
            cursor.execute("SELECT * FROM equipos ORDER BY id")

        return cursor.fetchall()

    except Error as e:
        messagebox.showerror("SQL", str(e))
        return []

    finally:
        cursor.close()
        conn.close()


def ModificarEquipo(id_e, nombre, ip, tipo, ubic, estado):
    conn = obtener_conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE equipos SET nombre=%s, ip=%s, tipo=%s, ubicacion=%s, estado=%s
            WHERE id=%s
        """, (nombre, ip, tipo, ubic, estado, id_e))
        conn.commit()
        return True

    except Error as e:
        messagebox.showerror("SQL", str(e))
        return False

    finally:
        cursor.close()
        conn.close()


def EliminarEquipo(id_e):
    conn = obtener_conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipos WHERE id=%s", (id_e,))
        conn.commit()
        return True

    except Error as e:
        messagebox.showerror("SQL", str(e))
        return False

    finally:
        cursor.close()
        conn.close()


def ip_existe(ip):
    conn = obtener_conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM equipos WHERE ip=%s", (ip,))
        return cursor.fetchone() is not None

    except:
        return False

    finally:
        cursor.close()
        conn.close()


def GenerarAlertas():
    return [e for e in MostrarInventario() if e["estado"].lower() != "online"]


# =============================================================================
# VECTORES Y MATRICES
# =============================================================================
def construir_vectores_y_matrices():
    datos = MostrarInventario()
    equipos = [d["nombre"] for d in datos]
    ubicaciones = list({d["ubicacion"] for d in datos})
    matriz = [[d["ip"], d["estado"]] for d in datos]
    return equipos, ubicaciones, matriz


# =============================================================================
# APLICACIÓN PRINCIPAL (NOTEBOOK)
# =============================================================================
class AppNotebook:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario de Equipos de Red – Notebook UI")
        self.root.geometry("1100x700")

        # Crear tabla en la BD
        crear_tabla()

        self.armar_interfaz()
        self.refrescar_tabla()
        self.refrescar_alertas()

    # -------------------------------------------------------------------------
    # Construcción del Notebook
    # -------------------------------------------------------------------------
    def armar_interfaz(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_registro = ttk.Frame(self.notebook)
        self.tab_inventario = ttk.Frame(self.notebook)
        self.tab_alertas = ttk.Frame(self.notebook)
        self.tab_herramientas = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_registro, text="Registro")
        self.notebook.add(self.tab_inventario, text="Inventario")
        self.notebook.add(self.tab_alertas, text="Alertas")
        self.notebook.add(self.tab_herramientas, text="Herramientas")

        self.build_tab_registro()
        self.build_tab_inventario()
        self.build_tab_alertas()
        self.build_tab_herramientas()

    # -------------------------------------------------------------------------
    # TAB REGISTRO – AJUSTADA Y AGRANDADA COMPLETAMENTE
    # -------------------------------------------------------------------------
    def build_tab_registro(self):

        main_frame = ttk.Frame(self.tab_registro)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        frm = ttk.LabelFrame(main_frame, text="Formulario de Registro", padding=20)
        frm.place(relx=0.5, rely=0.05, anchor="n", width=650, height=430)

        ttk.Label(frm, text="Nombre:").grid(row=0, column=0, sticky="w", pady=8)
        self.entry_nombre = ttk.Entry(frm, width=45)
        self.entry_nombre.grid(row=0, column=1, pady=8)

        ttk.Label(frm, text="IP:").grid(row=1, column=0, sticky="w", pady=8)
        self.entry_ip = ttk.Entry(frm, width=45)
        self.entry_ip.grid(row=1, column=1, pady=8)

        ttk.Label(frm, text="Tipo:").grid(row=2, column=0, sticky="w", pady=8)
        self.entry_tipo = ttk.Entry(frm, width=45)
        self.entry_tipo.grid(row=2, column=1, pady=8)

        ttk.Label(frm, text="Ubicación:").grid(row=3, column=0, sticky="w", pady=8)
        self.entry_ubic = ttk.Entry(frm, width=45)
        self.entry_ubic.grid(row=3, column=1, pady=8)

        ttk.Label(frm, text="Estado:").grid(row=4, column=0, sticky="w", pady=8)
        self.combo_estado = ttk.Combobox(frm,
                                         values=["online", "offline", "mantenimiento", "desconocido"],
                                         width=43, state="readonly")
        self.combo_estado.grid(row=4, column=1, pady=8)
        self.combo_estado.set("desconocido")

        btn_frame = ttk.Frame(frm)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=15)

        ttk.Button(btn_frame, text="Registrar", width=18,
                   command=self.registrar_equipo_gui).pack(side="left", padx=6)

        ttk.Button(btn_frame, text="Guardar Cambios", width=18,
                   command=self.guardar_cambios).pack(side="left", padx=6)

        ttk.Button(btn_frame, text="Limpiar", width=18,
                   command=self.limpiar_form).pack(side="left", padx=6)

    # -------------------------------------------------------------------------
    # TAB INVENTARIO
    # -------------------------------------------------------------------------
    def build_tab_inventario(self):

        top = ttk.Frame(self.tab_inventario)
        top.pack(fill="x", padx=12, pady=8)

        ttk.Label(top, text="Buscar por IP:").pack(side="left")
        self.search_ip = ttk.Entry(top, width=30)
        self.search_ip.pack(side="left", padx=6)

        ttk.Button(top, text="Buscar", command=self.buscar_por_ip).pack(side="left", padx=4)
        ttk.Button(top, text="Mostrar todo", command=self.refrescar_tabla).pack(side="left", padx=4)

        ttk.Button(top, text="Editar", command=self.cargar_equipo_edicion).pack(side="right", padx=4)
        ttk.Button(top, text="Eliminar", command=self.eliminar_equipo_gui).pack(side="right", padx=4)

        frame_tbl = ttk.Frame(self.tab_inventario)
        frame_tbl.pack(fill="both", expand=True, padx=12, pady=6)

        cols = ("id", "nombre", "ip", "tipo", "ubicacion", "estado", "fecha")
        self.tree = ttk.Treeview(frame_tbl, columns=cols, show="headings", height=18)

        for c in cols:
            self.tree.heading(c, text=c.upper())
            self.tree.column(c, width=140)

        self.tree.pack(side="left", fill="both", expand=True)

        vsb = ttk.Scrollbar(frame_tbl, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        vsb.pack(side="right", fill="y")

    # -------------------------------------------------------------------------
    # TAB ALERTAS
    # -------------------------------------------------------------------------
    def build_tab_alertas(self):
        frame = ttk.Frame(self.tab_alertas)
        frame.pack(fill="both", expand=True, padx=12, pady=12)

        ttk.Button(frame, text="Refrescar", command=self.refrescar_alertas).pack(anchor="ne")

        ttk.Label(frame, text="Equipos en alerta:",
                  font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=6)

        self.lb_alertas = tk.Listbox(frame, height=20)
        self.lb_alertas.pack(fill="both", expand=True)

    # -------------------------------------------------------------------------
    # TAB HERRAMIENTAS
    # -------------------------------------------------------------------------
    def build_tab_herramientas(self):
        frame = ttk.Frame(self.tab_herramientas)
        frame.pack(fill="both", expand=True, padx=12, pady=12)

        ttk.Button(frame, text="Exportar CSV",
                   command=self.exportar_csv).pack(anchor="nw", pady=6)

        ttk.Button(frame, text="Ver vectores y matriz",
                   command=self.mostrar_vectores_matriz).pack(anchor="nw", pady=6)

    # =============================================================================
    # FUNCIONES GUI – REGISTRO / EDITAR
    # =============================================================================
    def registrar_equipo_gui(self):
        n = self.entry_nombre.get().strip()
        ip = self.entry_ip.get().strip()
        t = self.entry_tipo.get().strip()
        u = self.entry_ubic.get().strip()
        e = self.combo_estado.get().strip()

        if not n or not ip:
            messagebox.showwarning("Validación", "Nombre e IP son obligatorios.")
            return

        partes = ip.split(".")
        if len(partes) != 4 or not all(p.isdigit() and 0 <= int(p) <= 255 for p in partes):
            messagebox.showwarning("Validación", "IP inválida.")
            return

        if ip_existe(ip):
            messagebox.showwarning("Validación", "La IP ya está registrada.")
            return

        equipo = Equipo(n, ip, t, u, e)

        if RegistrarEquipo(equipo):
            messagebox.showinfo("OK", "Equipo registrado.")
            self.refrescar_tabla()
            self.refrescar_alertas()
            self.limpiar_form()

    def cargar_equipo_edicion(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Editar", "Seleccione una fila.")
            return

        item = self.tree.item(sel)
        vals = item["values"]

        self.equipo_edit_id = vals[0]

        self.entry_nombre.delete(0, tk.END)
        self.entry_nombre.insert(0, vals[1])

        self.entry_ip.delete(0, tk.END)
        self.entry_ip.insert(0, vals[2])

        self.entry_tipo.delete(0, tk.END)
        self.entry_tipo.insert(0, vals[3])

        self.entry_ubic.delete(0, tk.END)
        self.entry_ubic.insert(0, vals[4])

        self.combo_estado.set(vals[5])

        self.notebook.select(self.tab_registro)
        messagebox.showinfo("Editar", "Modifique los campos y guarde los cambios.")

    def guardar_cambios(self):
        if not hasattr(self, "equipo_edit_id"):
            messagebox.showwarning("Modificar", "No hay equipo cargado.")
            return

        id_e = self.equipo_edit_id
        n = self.entry_nombre.get()
        ip = self.entry_ip.get()
        t = self.entry_tipo.get()
        u = self.entry_ubic.get()
        e = self.combo_estado.get()

        for r in MostrarInventario():
            if r["ip"] == ip and r["id"] != id_e:
                messagebox.showwarning("Validación", f"La IP {ip} ya está en uso.")
                return

        if ModificarEquipo(id_e, n, ip, t, u, e):
            messagebox.showinfo("OK", "Equipo actualizado.")
            self.refrescar_tabla()
            self.refrescar_alertas()
            self.limpiar_form()
            del self.equipo_edit_id

    # =============================================================================
    # FUNCIONES GUI – ELIMINAR, BUSCAR, CARGAR TABLA
    # =============================================================================
    def eliminar_equipo_gui(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Eliminar", "Seleccione un equipo.")
            return

        item = self.tree.item(sel)
        id_e = item["values"][0]

        if messagebox.askyesno("Confirmar", f"¿Eliminar equipo ID {id_e}?"):
            if EliminarEquipo(id_e):
                messagebox.showinfo("OK", "Eliminado.")
                self.refrescar_tabla()
                self.refrescar_alertas()

    def buscar_por_ip(self):
        ip = self.search_ip.get().strip()
        if not ip:
            messagebox.showwarning("Buscar", "Ingrese una IP.")
            return

        datos = MostrarInventario(ip)
        self.cargar_tabla(datos)
        self.notebook.select(self.tab_inventario)

    def cargar_tabla(self, datos):
        for f in self.tree.get_children():
            self.tree.delete(f)

        for r in datos:
            self.tree.insert("", tk.END, values=(
                r["id"], r["nombre"], r["ip"], r["tipo"],
                r["ubicacion"], r["estado"], r["fecha_registro"]
            ))

    def refrescar_tabla(self):
        self.cargar_tabla(MostrarInventario())

    # =============================================================================
    # ALERTAS
    # =============================================================================
    def refrescar_alertas(self):
        self.lb_alertas.delete(0, tk.END)
        for a in GenerarAlertas():
            texto = f"{a['id']} - {a['nombre']} - {a['ip']} - {a['estado']} ({a['ubicacion']})"
            self.lb_alertas.insert(tk.END, texto)

    # =============================================================================
    # EXPORTAR Y VECTORES/MATRIZ
    # =============================================================================
    def exportar_csv(self):
        datos = MostrarInventario()
        if not datos:
            messagebox.showinfo("Exportar", "No hay datos.")
            return

        nombre = f"inventario_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        with open(nombre, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["ID","Nombre","IP","Tipo","Ubicación","Estado","Fecha"])
            for r in datos:
                w.writerow([
                    r["id"], r["nombre"], r["ip"], r["tipo"],
                    r["ubicacion"], r["estado"], r["fecha_registro"]
                ])

        messagebox.showinfo("CSV", f"Archivo creado: {nombre}")

    def mostrar_vectores_matriz(self):
        equipos, ubicaciones, matriz = construir_vectores_y_matrices()

        texto = (
            f"Equipos:\n{equipos}\n\n"
            f"Ubicaciones:\n{ubicaciones}\n\n"
            "Matriz IP-Estado:\n"
        )

        for m in matriz:
            texto += f"{m}\n"

        top = tk.Toplevel(self.root)
        top.title("Vectores y Matriz")

        t = tk.Text(top, width=90, height=30)
        t.pack(padx=10, pady=10)
        t.insert("1.0", texto)
        t.config(state="disabled")

    # =============================================================================
    # LIMPIAR FORMULARIO
    # =============================================================================
    def limpiar_form(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_ip.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_ubic.delete(0, tk.END)
        self.combo_estado.set("desconocido")


# =============================================================================
# EJECUCIÓN
# =============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = AppNotebook(root)
    root.mainloop()
