# ==============================================================================
# EMPLEADOS.PY
# ==============================================================================

# Este módulo contiene la interfaz y la lógica CRUD de la pestaña Empleados. La ventana principal y el Notebook NO se crean aquí. Esos elementos pertenecen a interfaz.py.
## interfaz.py crea la pestaña y se la entrega a esta clase. La estructura general es:
#
#     main.py
#         ↓
#     interfaz.py
#         ↓
#     Notebook
#         ↓
#     pestaña Empleados
#         ↓
#     Empleados
#         ↓
#     formulario + Treeview + CRUD
#

# ==============================================================================
# 1. IMPORTACIONES
# ==============================================================================

# Tkinter permite crear la interfaz gráfica.
import tkinter as tk

# ttk es un módulo de Tkinter que proporciona widgets adicionales. En este módulo utilizamos Treeview para mostrar los registros de empleados dentro de la pestaña de Empleados.
from tkinter import ttk

# messagebox permite mostrar mensajes de información, error, advertencia y confirmación.
from tkinter import messagebox


# ==============================================================================
# 2. CLASE EMPLEADOS: sólo una en cada proyecto
# ==============================================================================

class Empleados:

    def __init__(self, pestana):

        # ----------------------------------------------------------------------
        # RECIBIMOS LA PESTAÑA
        # ----------------------------------------------------------------------

        # interfaz.py ya creó la pestaña correspondiente a Empleados. No creamos una nueva ventana Tk(). Tampoco creamos aquí el Notebook. Simplemente recibimos la pestaña como parámetro.
        self.pestana = pestana


        # ==========================================================================
        # 3. FORMULARIO DE EMPLEADOS
        # ==========================================================================

        # --------------------------------------------------------------------------
        # APELLIDO
        # --------------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="Apellido:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        # Entry permite introducir el apellido. Lo guardamos como atributo de la instancia porque las funciones CRUD necesitarán acceder posteriormente a este Entry.

        self.caja_apellido = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_apellido.grid(
            row=0,
            column=1,
            padx=5,
            pady=4
        )

        # --------------------------------------------------------------------------
        # NOMBRE
        # --------------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_nombre = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_nombre.grid(
            row=1,
            column=1,
            padx=5,
            pady=4
        )

        # --------------------------------------------------------------------------
        # DNI
        # --------------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="DNI:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_dni = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_dni.grid(
            row=2,
            column=1,
            padx=5,
            pady=4
        )

        # --------------------------------------------------------------------------
        # SUELDO BÁSICO
        # --------------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="Sueldo básico:"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_sueldo = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_sueldo.grid(
            row=3,
            column=1,
            padx=5,
            pady=4
        )

        # ==========================================================================
        # 4. TABLA DE EMPLEADOS
        # ==========================================================================

        # Definimos las columnas que tendrá el Treeview. # El orden es importante porque posteriormente accederemos a los valores mediante sus posiciones:
            # valores[0] → Apellido
            # valores[1] → Nombre
            # valores[2] → DNI
            # valores[3] → Sueldo básico
        columnas = (
            "Apellido",
            "Nombre",
            "DNI",
            "Sueldo básico"
        )

        # Creamos el Treeview dentro de la pestaña.
        self.tabla = ttk.Treeview(
            self.pestana,
            columns=columnas,
            show="headings",
            height=10
        )

        # Definimos el ancho de cada columna.
        anchos = [180, 180, 120, 140]

        # Configuramos cada columna. enumerate() permite obtener:
            # idx → posición de la columna
            # col → nombre de la columna
        for idx, col in enumerate(columnas):

            # Texto del encabezado.
            self.tabla.heading(
                col,
                text=col
            )

            # Ancho y alineación de la columna.
            self.tabla.column(
                col,
                width=anchos[idx],
                anchor="center"
            )


        # Ubicamos la tabla debajo del formulario.
        self.tabla.grid(
            row=5,
            column=0,
            columnspan=5,
            padx=15,
            pady=(10, 15),
            sticky="ew"
        )


        # ==========================================================================
        # 5. FUNCIONES CRUD
        # ==========================================================================

        # --------------------------------------------------------------------------
        # LIMPIAR CAMPOS
        # --------------------------------------------------------------------------

        def limpiar_campos():

            # delete() elimina el contenido del Entry.
            #
            # 0 representa la posición inicial.
            # tk.END representa el final del contenido.
            self.caja_apellido.delete(0, tk.END)
            self.caja_nombre.delete(0, tk.END)
            self.caja_dni.delete(0, tk.END)
            self.caja_sueldo.delete(0, tk.END)


        # --------------------------------------------------------------------------
        # NUEVO EMPLEADO
        # --------------------------------------------------------------------------

        def nuevo_empleado():

            # Limpiamos el formulario.
            limpiar_campos()

            # Quitamos cualquier selección de la tabla.
            self.tabla.selection_remove(
                self.tabla.selection()
            )

            # Colocamos el cursor en el primer campo.
            self.caja_apellido.focus()


        # --------------------------------------------------------------------------
        # CARGAR DATOS DE LA FILA SELECCIONADA
        # --------------------------------------------------------------------------

        def cargar_datos_seleccionados(event=None):

            # Obtenemos la fila seleccionada.
            seleccion = self.tabla.selection()


            # Si no hay selección, no hacemos nada.
            if not seleccion:
                return


            # Obtenemos el identificador de la primera fila.
            #
            # selection() devuelve una tupla.
            # seleccion[0] contiene el primer identificador.
            item_id = seleccion[0]


            # Obtenemos los valores almacenados en esa fila.
            valores = self.tabla.item(
                item_id,
                "values"
            )


            # Limpiamos primero los Entry.
            limpiar_campos()


            # Cargamos los valores de la tabla en el formulario.
            self.caja_apellido.insert(
                0,
                valores[0]
            )

            self.caja_nombre.insert(
                0,
                valores[1]
            )

            self.caja_dni.insert(
                0,
                valores[2]
            )

            self.caja_sueldo.insert(
                0,
                valores[3]
            )


        # --------------------------------------------------------------------------
        # GUARDAR EMPLEADO
        # --------------------------------------------------------------------------

        def guardar():

            # Obtenemos el contenido de cada Entry.
            #
            # get() obtiene el texto.
            # strip() elimina espacios al principio y al final.
            apellido = self.caja_apellido.get().strip()
            nombre = self.caja_nombre.get().strip()
            dni = self.caja_dni.get().strip()
            sueldo = self.caja_sueldo.get().strip()


            # ----------------------------------------------------------------------
            # VALIDACIÓN DE CAMPOS OBLIGATORIOS
            # ----------------------------------------------------------------------

            # Para este ejercicio consideramos obligatorios
            # el apellido y el DNI.
            if not apellido or not dni:

                messagebox.showerror(
                    "Error",
                    "Apellido y DNI son obligatorios.",
                    parent=self.pestana
                )

                return


            # ----------------------------------------------------------------------
            # VALIDACIÓN DEL DNI
            # ----------------------------------------------------------------------

            # isdigit() comprueba que todos los caracteres sean números.
            if not dni.isdigit():

                messagebox.showerror(
                    "Error",
                    "El DNI debe contener solamente números.",
                    parent=self.pestana
                )

                return


            # ----------------------------------------------------------------------
            # CONTROL DE DNI DUPLICADO
            # ----------------------------------------------------------------------

            # Recorremos todas las filas existentes.
            for item in self.tabla.get_children():

                # Obtenemos los valores de la fila actual.
                valores = self.tabla.item(
                    item,
                    "values"
                )


                # El DNI ocupa la posición 2.
                if valores[2] == dni:

                    messagebox.showerror(
                        "Error",
                        "Ya existe un empleado con ese DNI.",
                        parent=self.pestana
                    )

                    return


            # ----------------------------------------------------------------------
            # INSERTAR EMPLEADO
            # ----------------------------------------------------------------------

            # Insertamos una nueva fila al final de la tabla.
            self.tabla.insert(
                "",
                "end",
                values=(
                    apellido,
                    nombre,
                    dni,
                    sueldo
                )
            )


            # Informamos que la operación terminó correctamente.
            messagebox.showinfo(
                "Éxito",
                "Empleado guardado.",
                parent=self.pestana
            )


            # Limpiamos el formulario.
            limpiar_campos()


        # --------------------------------------------------------------------------
        # MODIFICAR EMPLEADO
        # --------------------------------------------------------------------------

        def modificar():

            # Comprobamos si existe una fila seleccionada.
            seleccion = self.tabla.selection()


            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona un empleado de la tabla para modificar.",
                    parent=self.pestana
                )

                return


            # Obtenemos el identificador de la fila.
            item_id = seleccion[0]


            # Obtenemos los valores actuales.
            valores = self.tabla.item(
                item_id,
                "values"
            )


            # ==========================================================================
            # VENTANA DE EDICIÓN
            # ==========================================================================

            # Toplevel crea una ventana secundaria.
            #
            # A diferencia de la ventana principal, esta ventana se utiliza
            # solamente para modificar el registro seleccionado.
            ventana_edicion = tk.Toplevel(
                self.pestana
            )

            ventana_edicion.title("Modificar Empleado")
            ventana_edicion.geometry("400x330")
            ventana_edicion.resizable(False, False)

            # La ventana queda asociada visualmente a la pestaña.
            ventana_edicion.transient(
                self.pestana
            )

            # grab_set() hace que el usuario deba terminar esta operación antes de volver a utilizar el resto de la interfaz.
            ventana_edicion.grab_set()

            # ----------------------------------------------------------------------
            # TÍTULO
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Modificar datos del empleado",
                font=("Arial", 12, "bold")
            ).pack(
                pady=(15, 10)
            )

            # ----------------------------------------------------------------------
            # APELLIDO
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Apellido:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_apellido = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_apellido.pack(
                padx=30,
                pady=(2, 6)
            )

            # Cargamos el apellido actual.
            caja_edicion_apellido.insert(
                0,
                valores[0]
            )

            # ----------------------------------------------------------------------
            # NOMBRE
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Nombre:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_nombre = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_nombre.pack(
                padx=30,
                pady=(2, 6)
            )

            caja_edicion_nombre.insert(
                0,
                valores[1]
            )

            # ----------------------------------------------------------------------
            # DNI
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="DNI:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_dni = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_dni.pack(
                padx=30,
                pady=(2, 6)
            )

            caja_edicion_dni.insert(
                0,
                valores[2]
            )

            # ----------------------------------------------------------------------
            # SUELDO BÁSICO
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Sueldo básico:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_sueldo = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_sueldo.pack(
                padx=30,
                pady=(2, 10)
            )

            caja_edicion_sueldo.insert(
                0,
                valores[3]
            )


            # ==========================================================================
            # GUARDAR MODIFICACIÓN
            # ==========================================================================

            # Esta función pertenece a la operación de modificación. Se ejecuta cuando el usuario pulsa "Guardar cambios".
            def guardar_modificacion():

                # Obtenemos los nuevos valores.
                apellido_mod = caja_edicion_apellido.get().strip()
                nombre_mod = caja_edicion_nombre.get().strip()
                dni_mod = caja_edicion_dni.get().strip()
                sueldo_mod = caja_edicion_sueldo.get().strip()

                # ------------------------------------------------------------------
                # VALIDACIÓN
                # ------------------------------------------------------------------

                if not apellido_mod or not dni_mod:

                    messagebox.showerror(
                        "Error",
                        "Apellido y DNI son obligatorios.",
                        parent=ventana_edicion
                    )

                    return


                # ------------------------------------------------------------------
                # VALIDACIÓN DEL DNI
                # ------------------------------------------------------------------

                if not dni_mod.isdigit():

                    messagebox.showerror(
                        "Error",
                        "El DNI debe contener solamente números.",
                        parent=ventana_edicion
                    )

                    return


                # ------------------------------------------------------------------
                # CONTROL DE DNI DUPLICADO
                # ------------------------------------------------------------------

                # Recorremos todas las filas existentes.
                for item in self.tabla.get_children():

                    # No comparamos la fila consigo misma.
                    if item == item_id:
                        continue

                    valores_otro = self.tabla.item(
                        item,
                        "values"
                    )

                    # Comprobamos si el nuevo DNI pertenece a otro empleado.
                    if valores_otro[2] == dni_mod:

                        messagebox.showerror(
                            "Error",
                            "Ya existe otro empleado con ese DNI.",
                            parent=ventana_edicion
                        )

                        return

                # ------------------------------------------------------------------
                # ACTUALIZAR LA FILA
                # ------------------------------------------------------------------

                # Reemplazamos los valores de la fila seleccionada.
                self.tabla.item(
                    item_id,
                    values=(
                        apellido_mod,
                        nombre_mod,
                        dni_mod,
                        sueldo_mod
                    )
                )

                # Cerramos la ventana de edición.
                ventana_edicion.destroy()

                # Informamos que la modificación terminó correctamente.
                messagebox.showinfo(
                    "Éxito",
                    "El empleado fue modificado correctamente.",
                    parent=self.pestana
                )

            # ==========================================================================
            # BOTONES DE LA VENTANA DE EDICIÓN
            # ==========================================================================

            marco_botones = tk.Frame(
                ventana_edicion
            )

            marco_botones.pack(
                pady=5
            )

            # ----------------------------------------------------------------------
            # GUARDAR CAMBIOS
            # ----------------------------------------------------------------------

            tk.Button(
                marco_botones,
                text="Guardar cambios",
                command=guardar_modificacion,
                width=16
            ).pack(
                side="left",
                padx=5
            )

            # ----------------------------------------------------------------------
            # CANCELAR
            # ----------------------------------------------------------------------

            # destroy() cierra la ventana sin modificar la fila.
            tk.Button(
                marco_botones,
                text="Cancelar",
                command=ventana_edicion.destroy,
                width=12
            ).pack(
                side="left",
                padx=5
            )

            # Colocamos el cursor en el primer campo.
            caja_edicion_apellido.focus()

        # --------------------------------------------------------------------------
        # ELIMINAR EMPLEADO
        # --------------------------------------------------------------------------

        def eliminar():
            # Obtenemos la fila seleccionada.
            seleccion = self.tabla.selection()

            # Si no hay selección, mostramos un aviso.
            if not seleccion:
                messagebox.showwarning(
                    "Atención",
                    "Selecciona un empleado de la tabla para eliminar.",
                    parent=self.pestana
                )
                return

            # Obtenemos el identificador de la fila.
            item_id = seleccion[0]

            # Obtenemos los valores de esa fila.
            valores = self.tabla.item(
                item_id,
                "values"
            )

            # Separamos los valores para mostrarlos en el mensaje de confirmación.
            apellido = valores[0]
            nombre = valores[1]
            dni = valores[2]
            sueldo = valores[3]

            # ----------------------------------------------------------------------
            # CONFIRMACIÓN DE LA BAJA
            # ----------------------------------------------------------------------

            confirmar = messagebox.askyesno(
                "Confirmar baja",
                f"¿Deseas eliminar el siguiente empleado?\n\n"
                f"Apellido: {apellido}\n"
                f"Nombre: {nombre}\n"
                f"DNI: {dni}\n"
                f"Sueldo básico: {sueldo}\n\n"
                f"Esta operación no se puede deshacer.",
                parent=self.pestana
            )

            # ----------------------------------------------------------------------
            # ELIMINAR LA FILA
            # ----------------------------------------------------------------------

            if confirmar:

                # Eliminamos solamente la fila seleccionada.
                self.tabla.delete(
                    item_id
                )

                # Limpiamos el formulario.
                limpiar_campos()

                # Informamos que la baja fue realizada.
                messagebox.showinfo(
                    "Baja realizada",
                    "El empleado fue eliminado correctamente.",
                    parent=self.pestana
                )

        # ==========================================================================
        # 6. ENLACE DEL EVENTO DE SELECCIÓN
        # ==========================================================================

        # Cuando el usuario selecciona una fila del Treeview, se ejecuta automáticamente cargar_datos_seleccionados(). event=None permite que la función pueda recibir el evento generado por Tkinter.
        self.tabla.bind(
            "<<TreeviewSelect>>",
            cargar_datos_seleccionados
        )

        # ==========================================================================
        # 7. BOTONES DE OPERACIONES CRUD
        # ==========================================================================

        # --------------------------------------------------------------------------
        # NUEVO EMPLEADO
        # --------------------------------------------------------------------------

        tk.Button(
            self.pestana,
            text="Nuevo empleado",
            command=nuevo_empleado,
            width=16
        ).grid(
            row=0,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )

        # --------------------------------------------------------------------------
        # GUARDAR EMPLEADO
        # --------------------------------------------------------------------------

        tk.Button(
            self.pestana,
            text="Guardar empleado",
            command=guardar,
            width=16
        ).grid(
            row=1,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )

        # --------------------------------------------------------------------------
        # MODIFICAR EMPLEADO
        # --------------------------------------------------------------------------

        tk.Button(
            self.pestana,
            text="Modificar empleado",
            command=modificar,
            width=16
        ).grid(
            row=2,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )

        # --------------------------------------------------------------------------
        # ELIMINAR EMPLEADO
        # --------------------------------------------------------------------------

        tk.Button(
            self.pestana,
            text="Eliminar empleado",
            command=eliminar,
            width=16
        ).grid(
            row=3,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )