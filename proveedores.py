# proveedores.py

# Responsabilidad del módulo: Construir y administrar el contenido de la pestaña "Proveedores".
# Este módulo NO crea (esa infraestructura pertenece a interfaz.py)
#   - la ventana principal Tk()
#   - el Notebook
#   - las pestañas

# Este módulo recibe la pestaña correspondiente y construye dentro de ella:
#   1. El formulario de proveedores.
#   2. El Treeview para mostrar los registros.
#   3. Las funciones CRUD.
#   4. El enlace entre selección y formulario.
#   5. Los botones de operaciones.

# ==============================================================================
# 1. IMPORTACIONES
# ==============================================================================
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# ------------------------------------------------------------------------------
# tk: Proporciona los widgets básicos de Tkinter:
#   Label  → etiquetas
#   Entry  → cajas de entrada
#   Button → botones

# Recordar: tk no "maneja al usuario" por sí mismo. Los widgets reciben acciones del usuario y los eventos son procesados por el bucle principal de Tkinter.
# ------------------------------------------------------------------------------
# ttk: Proporciona widgets adicionales de Tkinter.
# En este módulo utilizamos Treeview → mostrar los registros de proveedores.
# Recordar: Entry y Treeview cumplen funciones diferentes:
#   Entry     → introducir / editar datos.
#   Treeview  → mostrar registros.
# ------------------------------------------------------------------------------
# messagebox: Permite mostrar mensajes emergentes:
#   showinfo()    → información
#   showwarning() → advertencia
#   showerror()   → error
#   askyesno()    → confirmación

# ==============================================================================
# 2. CLASE PROVEEDORES
# ==============================================================================
class Proveedores:

    def __init__(self, pestana):
        # ----------------------------------------------------------------------
        # RECIBIR LA PESTAÑA
        # "pestana" es un parámetro. interfaz.py creó esta pestaña y se la entrega a la clase.
        # No hacemos tk.Tk() porque ya existe una ventana principal. Tampoco creamos aquí un Notebook.
        # La clase trabaja dentro del espacio que recibió.
        # ----------------------------------------------------------------------

        self.pestana = pestana

        # ==========================================================================
        # 3. FORMULARIO DE PROVEEDORES
        # ==========================================================================

        # ----------------------------------------------------------------------
        # RAZÓN SOCIAL
        # ----------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="Razón Social:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_razon_social = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_razon_social.grid(
            row=0,
            column=1,
            padx=5,
            pady=4
        )

        # ----------------------------------------------------------------------
        # CONTACTO
        # ----------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="Contacto:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_contacto = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_contacto.grid(
            row=1,
            column=1,
            padx=5,
            pady=4
        )


        # ----------------------------------------------------------------------
        # CUIT
        # ----------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="CUIT:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_cuit = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_cuit.grid(
            row=2,
            column=1,
            padx=5,
            pady=4
        )

        # ==========================================================================
        # 4. TREEVIEW
        # ==========================================================================

        # Las columnas representan los datos que queremos mostrar.
        #
        # Importante: estas columnas deben mantener el mismo orden que utilizaremos posteriormente al insertar y recuperar registros.

        columnas = (
            "Razón Social",
            "Contacto",
            "CUIT"
        )

        self.tabla = ttk.Treeview(
            self.pestana,
            columns=columnas,
            show="headings",
            height=10
        )

        # ----------------------------------------------------------------------
        # CONFIGURACIÓN DE LAS COLUMNAS
        # ----------------------------------------------------------------------

        anchos = [250, 200, 150]

        for idx, columna in enumerate(columnas):
            # Texto que aparece en el encabezado.
            self.tabla.heading(
                columna,
                text=columna
            )
            # Configuración visual de cada columna.
            self.tabla.column(
                columna,
                width=anchos[idx],
                anchor="center"
            )

        # ----------------------------------------------------------------------
        # UBICACIÓN DEL TREEVIEW
        # ----------------------------------------------------------------------

        self.tabla.grid(
            row=6,
            column=0,
            columnspan=5,
            padx=15,
            pady=(10, 15),
            sticky="ew"
        )

        # ==========================================================================
        # 5. FUNCIONES AUXILIARES Y CRUD
        # ==========================================================================

        # ----------------------------------------------------------------------
        # LIMPIAR CAMPOS
        # Función auxiliar. No pertenece directamente a CRUD. Su objetivo es preparar el formulario.
        # ----------------------------------------------------------------------

        def limpiar_campos():

            self.caja_razon_social.delete(
                0,
                tk.END
            )

            self.caja_contacto.delete(
                0,
                tk.END
            )

            self.caja_cuit.delete(
                0,
                tk.END
            )

        # ----------------------------------------------------------------------
        # NUEVO PROVEEDOR
        # ----------------------------------------------------------------------
        #
        # Prepara el formulario para una nueva carga.
        # IMPORTANTE:
        # "Nuevo" no guarda nada. Solamente prepara la interfaz.
        # ----------------------------------------------------------------------

        def nuevo_proveedor():

            limpiar_campos()

            # Eliminamos cualquier selección existente.
            self.tabla.selection_remove(
                self.tabla.selection()
            )

            # Colocamos el cursor en el primer campo.
            self.caja_razon_social.focus()


        # ----------------------------------------------------------------------
        # READ: CARGAR DATOS DE LA FILA SELECCIONADA
        # ----------------------------------------------------------------------
        #
        # Recupera los valores de una fila del Treeview y los coloca nuevamente en los Entry. Este mecanismo será utilizado al seleccionar un proveedor.
        # ----------------------------------------------------------------------

        def cargar_datos_seleccionados(event=None):

            seleccion = self.tabla.selection()

            if not seleccion:
                return

            # Treeview.selection() devuelve los identificadores
            # de las filas seleccionadas.
            #
            # Tomamos el primer identificador.
            item_id = seleccion[0]

            # Recuperamos los valores almacenados en esa fila.
            valores = self.tabla.item(
                item_id,
                "values"
            )

            limpiar_campos()

            # Los índices deben coincidir con el orden de las columnas.
            self.caja_razon_social.insert(
                0,
                valores[0]
            )

            self.caja_contacto.insert(
                0,
                valores[1]
            )

            self.caja_cuit.insert(
                0,
                valores[2]
            )

        # ----------------------------------------------------------------------
        # CREATE: GUARDAR PROVEEDOR
        # ----------------------------------------------------------------------

        def guardar():

            # Obtenemos el contenido de los Entry.
            # get() → obtiene el texto.
            # strip() → elimina espacios al principio y al final.

            razon_social = self.caja_razon_social.get().strip()
            contacto = self.caja_contacto.get().strip()
            cuit = self.caja_cuit.get().strip()

            # ------------------------------------------------------------------
            # VALIDACIÓN
            # ------------------------------------------------------------------

            if not razon_social or not cuit:

                messagebox.showerror(
                    "Error",
                    "Razón Social y CUIT son obligatorios.",
                    parent=self.pestana
                )

                return

            # ------------------------------------------------------------------
            # CONTROL DEL CUIT
            # ------------------------------------------------------------------

            if not cuit.isdigit():

                messagebox.showerror(
                    "Error",
                    "El CUIT debe contener solamente números.",
                    parent=self.pestana
                )

                return

            # ------------------------------------------------------------------
            # CONTROL DE DUPLICADOS
            # ------------------------------------------------------------------

            for item in self.tabla.get_children():

                valores = self.tabla.item(
                    item,
                    "values"
                )

                if valores[2] == cuit:

                    messagebox.showerror(
                        "Error",
                        "Ya existe un proveedor con ese CUIT.",
                        parent=self.pestana
                    )

                    return

            # ------------------------------------------------------------------
            # INSERTAR REGISTRO
            # ------------------------------------------------------------------
            #
            # Aquí ocurre realmente el CREATE.
            # ------------------------------------------------------------------

            self.tabla.insert(
                "",
                "end",
                values=(
                    razon_social,
                    contacto,
                    cuit
                )
            )


            messagebox.showinfo(
                "Éxito",
                "Proveedor guardado.",
                parent=self.pestana
            )

            limpiar_campos()

        # ----------------------------------------------------------------------
        # UPDATE: MODIFICAR PROVEEDOR
        # ----------------------------------------------------------------------

        def modificar():

            seleccion = self.tabla.selection()

            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona un proveedor de la tabla para modificar.",
                    parent=self.pestana
                )

                return


            # Identificador interno de la fila.
            item_id = seleccion[0]


            # Valores actuales de la fila.
            valores = self.tabla.item(
                item_id,
                "values"
            )


            # ------------------------------------------------------------------
            # VENTANA DE EDICIÓN
            # ------------------------------------------------------------------
            #
            # Esta es una función dentro de otra función.
            #
            # La ventana pertenece conceptualmente a "modificar".
            # ------------------------------------------------------------------

            ventana_edicion = tk.Toplevel(
                self.pestana
            )

            ventana_edicion.title(
                "Modificar Proveedor"
            )

            ventana_edicion.geometry(
                "400x280"
            )

            ventana_edicion.resizable(
                False,
                False
            )

            # Hace que la ventana de edición quede asociada a la pestaña.
            ventana_edicion.transient(
                self.pestana
            )

            # Impide interactuar con la ventana principal mientras
            # la edición está abierta.
            ventana_edicion.grab_set()


            # ------------------------------------------------------------------
            # CAMPOS DE EDICIÓN
            # ------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Modificar datos del proveedor",
                font=("Arial", 12, "bold")
            ).pack(
                pady=(15, 10)
            )


            tk.Label(
                ventana_edicion,
                text="Razón Social:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_razon = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_razon.pack(
                padx=30,
                pady=(2, 8)
            )

            caja_edicion_razon.insert(
                0,
                valores[0]
            )


            tk.Label(
                ventana_edicion,
                text="Contacto:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_contacto = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_contacto.pack(
                padx=30,
                pady=(2, 8)
            )

            caja_edicion_contacto.insert(
                0,
                valores[1]
            )


            tk.Label(
                ventana_edicion,
                text="CUIT:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_cuit = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_cuit.pack(
                padx=30,
                pady=(2, 12)
            )

            caja_edicion_cuit.insert(
                0,
                valores[2]
            )


            # ------------------------------------------------------------------
            # GUARDAR MODIFICACIÓN
            # ------------------------------------------------------------------
            #
            # Función anidada:
            #
            #     modificar()
            #          └── guardar_modificacion()
            #
            # Se utiliza aquí porque esta función solamente tiene sentido
            # mientras existe la ventana de edición.
            # ------------------------------------------------------------------

            def guardar_modificacion():

                razon_mod = caja_edicion_razon.get().strip()
                contacto_mod = caja_edicion_contacto.get().strip()
                cuit_mod = caja_edicion_cuit.get().strip()


                # Validación de datos obligatorios.

                if not razon_mod or not cuit_mod:

                    messagebox.showerror(
                        "Error",
                        "Razón Social y CUIT son obligatorios.",
                        parent=ventana_edicion
                    )

                    return


                # Validación del CUIT.

                if not cuit_mod.isdigit():

                    messagebox.showerror(
                        "Error",
                        "El CUIT debe contener solamente números.",
                        parent=ventana_edicion
                    )

                    return


                # Controlamos que el nuevo CUIT no pertenezca
                # a otro registro.

                for item in self.tabla.get_children():

                    # No comparamos la fila consigo misma.
                    if item == item_id:
                        continue

                    valores_otro = self.tabla.item(
                        item,
                        "values"
                    )

                    if valores_otro[2] == cuit_mod:

                        messagebox.showerror(
                            "Error",
                            "Ya existe otro proveedor con ese CUIT.",
                            parent=ventana_edicion
                        )

                        return


                # --------------------------------------------------------------
                # ACTUALIZAR LA FILA
                # --------------------------------------------------------------

                self.tabla.item(
                    item_id,
                    values=(
                        razon_mod,
                        contacto_mod,
                        cuit_mod
                    )
                )


                ventana_edicion.destroy()

                messagebox.showinfo(
                    "Éxito",
                    "El proveedor fue modificado correctamente.",
                    parent=self.pestana
                )


            # ------------------------------------------------------------------
            # BOTONES DE LA VENTANA DE EDICIÓN
            # ------------------------------------------------------------------

            marco_botones = tk.Frame(
                ventana_edicion
            )

            marco_botones.pack(
                pady=5
            )


            tk.Button(
                marco_botones,
                text="Guardar cambios",
                command=guardar_modificacion,
                width=16
            ).pack(
                side="left",
                padx=5
            )


            tk.Button(
                marco_botones,
                text="Cancelar",
                command=ventana_edicion.destroy,
                width=12
            ).pack(
                side="left",
                padx=5
            )


            caja_edicion_razon.focus()


        # ----------------------------------------------------------------------
        # DELETE: ELIMINAR PROVEEDOR
        # ----------------------------------------------------------------------

        def eliminar():

            seleccion = self.tabla.selection()

            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona un proveedor de la tabla para eliminar.",
                    parent=self.pestana
                )

                return


            item_id = seleccion[0]

            valores = self.tabla.item(
                item_id,
                "values"
            )


            razon_social = valores[0]
            contacto = valores[1]
            cuit = valores[2]


            # --------------------------------------------------------------
            # CONFIRMACIÓN
            # --------------------------------------------------------------

            confirmar = messagebox.askyesno(
                "Confirmar baja",
                f"¿Deseas eliminar el siguiente proveedor?\n\n"
                f"Razón Social: {razon_social}\n"
                f"Contacto: {contacto}\n"
                f"CUIT: {cuit}\n\n"
                f"Esta operación no se puede deshacer.",
                parent=self.pestana
            )


            # --------------------------------------------------------------
            # ELIMINACIÓN
            # --------------------------------------------------------------

            if confirmar:

                self.tabla.delete(
                    item_id
                )

                limpiar_campos()

                messagebox.showinfo(
                    "Baja realizada",
                    "El proveedor fue eliminado correctamente.",
                    parent=self.pestana
                )


        # ==========================================================================
        # 6. ENLACE DEL EVENTO DE SELECCIÓN
        # ==========================================================================

        # bind() relaciona un evento de Tkinter con una función.
        #
        # En este caso:
        #
        #     evento → selección de una fila
        #     función → cargar_datos_seleccionados
        #
        # Por lo tanto, cuando el usuario selecciona una fila,
        # los datos pasan del Treeview al formulario.

        self.tabla.bind(
            "<<TreeviewSelect>>",
            cargar_datos_seleccionados
        )


        # ==========================================================================
        # 7. BOTONES CRUD
        # ==========================================================================

        # ----------------------------------------------------------------------
        # NUEVO
        # ----------------------------------------------------------------------

        tk.Button(
            self.pestana,
            text="Nuevo Proveedor",
            command=nuevo_proveedor,
            width=16
        ).grid(
            row=0,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )


        # ----------------------------------------------------------------------
        # GUARDAR
        # ----------------------------------------------------------------------

        tk.Button(
            self.pestana,
            text="Guardar Proveedor",
            command=guardar,
            width=16
        ).grid(
            row=1,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )


        # ----------------------------------------------------------------------
        # MODIFICAR
        # ----------------------------------------------------------------------

        tk.Button(
            self.pestana,
            text="Modificar Proveedor",
            command=modificar,
            width=16
        ).grid(
            row=2,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )


        # ----------------------------------------------------------------------
        # ELIMINAR
        # ----------------------------------------------------------------------

        tk.Button(
            self.pestana,
            text="Eliminar Proveedor",
            command=eliminar,
            width=16
        ).grid(
            row=3,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )