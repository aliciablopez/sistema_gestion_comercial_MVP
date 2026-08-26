# ==============================================================================
# clientes.py (módulo de la pestaña clientes=
# ==============================================================================

# Este módulo contiene todo lo relacionado con la pestaña Clientes:
##   - formulario de carga
#   - Treeview para mostrar los clientes
#   - operaciones CRUD
#   - selección de registros
#   - modificación
#   - eliminación
#
# IMPORTANTE: Este módulo NO crea la ventana principal de Tkinter. Tampoco crea el Notebook. Tampoco ejecuta mainloop(). Esas responsabilidades pertenecen a interfaz.py.

# ==============================================================================
# 1. IMPORTACIONES
# ==============================================================================
# tkinter proporciona los elementos básicos de la interfaz gráfica: Label, Entry, Button, Frame, etc.
import tkinter as tk

# ttk proporciona widgets adicionales de Tkinter. En este módulo utilizamos Treeview para mostrar los clientes.
from tkinter import ttk

# messagebox permite mostrar ventanas emergentes con:
#   - errores
#   - advertencias
#   - información
#   - confirmaciones
from tkinter import messagebox

# ==============================================================================
# 2. CLASE / PESTAÑA DE CLIENTES
# ==============================================================================

# interfaz.py ya creó la ventana principal, el notebook y la pestaña de Clientes.Por eso este módulo recibe directamente la pestaña. Los demás módulos conservan esta estructura.
#       Clientes(pestana). La clase construye TODO el contenido dentro de esa pestaña.


class Clientes:

    def __init__(self, pestana):

        # Guardamos la referencia a la pestaña. "self" representa la instancia actual de Clientes. self.pestana permite que los métodos y funciones de esta instancia puedan utilizar posteriormente esa misma pestaña.

        self.pestana = pestana

        # ==========================================================================
        # 3. FORMULARIO DE CLIENTES
        # ==========================================================================

        # --------------------------------------------------------------------------
        # RAZÓN SOCIAL
        # --------------------------------------------------------------------------

        # Label muestra el texto que identifica al campo.
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

        # Entry es la caja donde el usuario introduce el dato.

        caja_razon_social = tk.Entry(
            self.pestana,
            width=25
        )

        # grid coloca la caja dentro de la pestaña. (row = fila, column = columna)
        caja_razon_social.grid(
            row=0,
            column=1,
            padx=5,
            pady=4
        )

        # --------------------------------------------------------------------------
        # CONTACTO
        # --------------------------------------------------------------------------

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
        caja_contacto = tk.Entry(
            self.pestana,
            width=25
        )
        caja_contacto.grid(
            row=1,
            column=1,
            padx=5,
            pady=4
        )

        # --------------------------------------------------------------------------
        # CUIT
        # --------------------------------------------------------------------------

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
        caja_cuit = tk.Entry(
            self.pestana,
            width=25
        )
        caja_cuit.grid(
            row=2,
            column=1,
            padx=5,
            pady=4
        )

        # ==========================================================================
        # 4. TREEVIEW
        # ==========================================================================

        # Treeview representa la tabla donde se muestran los registros.
        #
        # El formulario utiliza Entry para introducir datos.
        #
        # Treeview permite visualizar los clientes registrados.

        columnas = (
            "Razón Social",
            "Contacto",
            "CUIT"
        )


        # Creamos el Treeview.

        tabla = ttk.Treeview(
            self.pestana,
            columns=columnas,
            show="headings",
            height=10
        )


        # Ancho de cada columna.

        anchos = [
            250,
            200,
            150
        ]


        # Configuramos cada columna.

        for indice, columna in enumerate(columnas):

            # heading define el encabezado visible.

            tabla.heading(
                columna,
                text=columna
            )


            # column define las características de la columna.

            tabla.column(
                columna,
                width=anchos[indice],
                anchor="center"
            )


        # Colocamos la tabla debajo del formulario.

        tabla.grid(
            row=6,
            column=0,
            columnspan=5,
            padx=15,
            pady=(10, 15),
            sticky="ew"
        )


        # ==========================================================================
        # 5. FUNCIONES CRUD
        # ==========================================================================

        # CRUD significa:
        #
        # C = Create  → crear
        # R = Read    → leer / consultar
        # U = Update  → modificar
        # D = Delete  → eliminar
        #
        # En esta etapa las operaciones trabajan directamente sobre Treeview.
        #
        # En una futura versión BP, los datos estarán separados de la interfaz.


        # --------------------------------------------------------------------------
        # LIMPIAR CAMPOS
        # --------------------------------------------------------------------------

        def limpiar_campos():

            # delete(0, tk.END) elimina el contenido completo del Entry.
            #
            # 0 representa el comienzo del texto.
            # tk.END representa el final.

            caja_razon_social.delete(
                0,
                tk.END
            )


            caja_contacto.delete(
                0,
                tk.END
            )


            caja_cuit.delete(
                0,
                tk.END
            )


        # --------------------------------------------------------------------------
        # NUEVO CLIENTE
        # --------------------------------------------------------------------------

        def nuevo_cliente():

            # Limpiamos el formulario.

            limpiar_campos()


            # Quitamos cualquier selección existente en el Treeview.

            tabla.selection_remove(
                tabla.selection()
            )


            # Colocamos el cursor en el primer campo.

            caja_razon_social.focus()


        # --------------------------------------------------------------------------
        # CARGAR DATOS DE LA FILA SELECCIONADA
        # --------------------------------------------------------------------------

        def cargar_datos_seleccionados(event=None):

            # CAMBIO:
            #
            # Agregamos "event=None" porque esta función será llamada
            # mediante bind().
            #
            # bind() envía automáticamente un objeto evento.
            #
            # Nosotros no necesitamos utilizar ese objeto, pero la función
            # debe estar preparada para recibirlo.

            # Obtenemos la selección actual del Treeview.

            seleccion = tabla.selection()


            # Si no hay ninguna fila seleccionada, no hacemos nada.

            if not seleccion:
                return


            # Obtenemos el identificador de la fila.
            #
            # El usuario NO escribe este identificador.
            # Treeview lo genera automáticamente.

            item_id = seleccion[0]


            # Recuperamos los valores almacenados en esa fila.

            valores = tabla.item(
                item_id,
                "values"
            )


            # Limpiamos primero los Entry.

            limpiar_campos()


            # Cargamos los datos de la fila seleccionada
            # nuevamente en el formulario.

            caja_razon_social.insert(
                0,
                valores[0]
            )


            caja_contacto.insert(
                0,
                valores[1]
            )


            caja_cuit.insert(
                0,
                valores[2]
            )


        # --------------------------------------------------------------------------
        # GUARDAR CLIENTE
        # --------------------------------------------------------------------------

        def guardar():

            # get() obtiene el contenido de cada Entry.
            #
            # strip() elimina espacios innecesarios al principio y al final.

            razon_social = caja_razon_social.get().strip()
            contacto = caja_contacto.get().strip()
            cuit = caja_cuit.get().strip()


            # ----------------------------------------------------------------------
            # VALIDACIÓN DE CAMPOS OBLIGATORIOS
            # ----------------------------------------------------------------------

            # Razón Social y CUIT son obligatorios.

            if not razon_social or not cuit:

                messagebox.showerror(
                    "Error",
                    "Razón Social y CUIT son obligatorios.",
                    parent=self.pestana
                )

                return


            # ----------------------------------------------------------------------
            # VALIDACIÓN DEL CUIT
            # ----------------------------------------------------------------------

            # isdigit() comprueba que el texto contenga solamente dígitos.

            if not cuit.isdigit():

                messagebox.showerror(
                    "Error",
                    "El CUIT debe contener solamente números.",
                    parent=self.pestana
                )

                return


            # ----------------------------------------------------------------------
            # CONTROL DE DUPLICADOS
            # ----------------------------------------------------------------------

            # Recorremos todas las filas existentes.

            for item in tabla.get_children():

                # Recuperamos los valores de cada fila.

                valores = tabla.item(
                    item,
                    "values"
                )


                # El CUIT ocupa la posición 2:
                #
                # valores[0] → Razón Social
                # valores[1] → Contacto
                # valores[2] → CUIT

                if valores[2] == cuit:

                    messagebox.showerror(
                        "Error",
                        "Ya existe un cliente con ese CUIT.",
                        parent=self.pestana
                    )

                    return


            # ----------------------------------------------------------------------
            # INSERTAR EL CLIENTE
            # ----------------------------------------------------------------------

            tabla.insert(
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
                "Cliente guardado.",
                parent=self.pestana
            )


            # Dejamos el formulario preparado para cargar otro cliente.

            limpiar_campos()


        # --------------------------------------------------------------------------
        # MODIFICAR CLIENTE
        # --------------------------------------------------------------------------

        def modificar():

            # Obtenemos la selección del Treeview.

            seleccion = tabla.selection()


            # Si no hay selección, no podemos saber qué cliente modificar.

            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona un cliente para modificar.",
                    parent=self.pestana
                )

                return


            # Obtenemos el identificador de la fila seleccionada.

            item_id = seleccion[0]


            # Recuperamos los valores actuales.

            valores = tabla.item(
                item_id,
                "values"
            )


            # ==========================================================================
            # VENTANA EMERGENTE DE EDICIÓN
            # ==========================================================================

            # Toplevel crea una ventana secundaria.
            #
            # NO es otra aplicación.
            # Pertenece a la ventana principal existente.

            ventana_edicion = tk.Toplevel(
                self.pestana
            )


            ventana_edicion.title(
                "Modificar Cliente"
            )


            ventana_edicion.geometry(
                "400x280"
            )


            ventana_edicion.resizable(
                False,
                False
            )


            # La ventana queda asociada a la pestaña.

            ventana_edicion.transient(
                self.pestana
            )


            # grab_set() hace que la ventana de edición sea modal.
            #
            # El usuario debe terminar o cancelar la edición
            # antes de volver a trabajar con la pestaña.

            ventana_edicion.grab_set()


            # ----------------------------------------------------------------------
            # TÍTULO
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Modificar datos del cliente",
                font=("Arial", 12, "bold")
            ).pack(
                pady=(15, 10)
            )


            # ----------------------------------------------------------------------
            # RAZÓN SOCIAL
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Razón Social:"
            ).pack(
                anchor="w",
                padx=30
            )


            caja_razon_edicion = tk.Entry(
                ventana_edicion,
                width=40
            )


            caja_razon_edicion.pack(
                padx=30,
                pady=(2, 8)
            )


            # Cargamos el valor actual.

            caja_razon_edicion.insert(
                0,
                valores[0]
            )


            # ----------------------------------------------------------------------
            # CONTACTO
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Contacto:"
            ).pack(
                anchor="w",
                padx=30
            )


            caja_contacto_edicion = tk.Entry(
                ventana_edicion,
                width=40
            )


            caja_contacto_edicion.pack(
                padx=30,
                pady=(2, 8)
            )


            caja_contacto_edicion.insert(
                0,
                valores[1]
            )


            # ----------------------------------------------------------------------
            # CUIT
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="CUIT:"
            ).pack(
                anchor="w",
                padx=30
            )


            caja_cuit_edicion = tk.Entry(
                ventana_edicion,
                width=40
            )


            caja_cuit_edicion.pack(
                padx=30,
                pady=(2, 12)
            )


            caja_cuit_edicion.insert(
                0,
                valores[2]
            )


            # ==========================================================================
            # GUARDAR MODIFICACIÓN
            # ==========================================================================

            # Esta función está ANIDADA dentro de modificar().
            #
            # Su función es guardar los cambios realizados
            # específicamente en la ventana de edición.

            def guardar_modificacion():

                razon_social = caja_razon_edicion.get().strip()
                contacto = caja_contacto_edicion.get().strip()
                cuit = caja_cuit_edicion.get().strip()


                # ----------------------------------------------------------------------
                # VALIDACIONES
                # ----------------------------------------------------------------------

                if not razon_social or not cuit:

                    messagebox.showerror(
                        "Error",
                        "Razón Social y CUIT son obligatorios.",
                        parent=ventana_edicion
                    )

                    return


                if not cuit.isdigit():

                    messagebox.showerror(
                        "Error",
                        "El CUIT debe contener solamente números.",
                        parent=ventana_edicion
                    )

                    return


                # ----------------------------------------------------------------------
                # CONTROL DE CUIT DUPLICADO
                # ----------------------------------------------------------------------

                # Recorremos las filas existentes.

                for item in tabla.get_children():

                    # IMPORTANTE:
                    #
                    # La fila que estamos modificando ya tiene ese CUIT.
                    #
                    # Por eso no debemos compararla consigo misma.

                    if item == item_id:
                        continue


                    valores_otro = tabla.item(
                        item,
                        "values"
                    )


                    if valores_otro[2] == cuit:

                        messagebox.showerror(
                            "Error",
                            "Ya existe otro cliente con ese CUIT.",
                            parent=ventana_edicion
                        )

                        return


                # ----------------------------------------------------------------------
                # ACTUALIZAR LA FILA
                # ----------------------------------------------------------------------

                # item_id identifica exactamente la fila que queremos modificar.

                tabla.item(
                    item_id,
                    values=(
                        razon_social,
                        contacto,
                        cuit
                    )
                )


                # Cerramos la ventana de edición.

                ventana_edicion.destroy()


                messagebox.showinfo(
                    "Éxito",
                    "El cliente fue modificado correctamente.",
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


            # Botón para guardar los cambios.

            tk.Button(
                marco_botones,
                text="Guardar cambios",
                command=guardar_modificacion,
                width=16
            ).pack(
                side="left",
                padx=5
            )


            # Botón para cancelar.
            #
            # destroy() cierra la ventana de edición.

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

            caja_razon_edicion.focus()


        # --------------------------------------------------------------------------
        # ELIMINAR CLIENTE
        # --------------------------------------------------------------------------

        def eliminar():

            # Obtenemos la fila seleccionada.

            seleccion = tabla.selection()


            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona un cliente para eliminar.",
                    parent=self.pestana
                )

                return


            # Identificador de la fila.

            item_id = seleccion[0]


            # Valores de la fila.

            valores = tabla.item(
                item_id,
                "values"
            )


            razon_social = valores[0]
            contacto = valores[1]
            cuit = valores[2]


            # ----------------------------------------------------------------------
            # CONFIRMACIÓN
            # ----------------------------------------------------------------------

            confirmar = messagebox.askyesno(
                "Confirmar baja",
                f"¿Deseas eliminar este cliente?\n\n"
                f"Razón Social: {razon_social}\n"
                f"Contacto: {contacto}\n"
                f"CUIT: {cuit}\n\n"
                f"Esta operación no se puede deshacer.",
                parent=self.pestana
            )


            # ----------------------------------------------------------------------
            # ELIMINACIÓN
            # ----------------------------------------------------------------------

            if confirmar:

                tabla.delete(
                    item_id
                )


                limpiar_campos()


                messagebox.showinfo(
                    "Baja realizada",
                    "El cliente fue eliminado correctamente.",
                    parent=self.pestana
                )


        # ==========================================================================
        # 6. ENLACE DE SELECCIÓN
        # ==========================================================================

        # Treeview detecta que el usuario seleccionó una fila.
        #
        # bind() conecta ese evento con nuestra función.
        #
        # La secuencia es:
        #
        # Treeview
        #     ↓
        # selección
        #     ↓
        # <<TreeviewSelect>>
        #     ↓
        # bind()
        #     ↓
        # cargar_datos_seleccionados()
        #     ↓
        # Entry
        #
        # De esta manera los datos de la fila seleccionada
        # vuelven a aparecer en el formulario.

        tabla.bind(
            "<<TreeviewSelect>>",
            cargar_datos_seleccionados
        )


        # ==========================================================================
        # 7. BOTONES CRUD
        # ==========================================================================

        # Botón para comenzar la carga de un nuevo cliente.

        tk.Button(
            self.pestana,
            text="Nuevo Cliente",
            command=nuevo_cliente,
            width=16
        ).grid(
            row=0,
            column=4,
            padx=15,
            pady=2
        )


        # Botón para guardar.

        tk.Button(
            self.pestana,
            text="Guardar Cliente",
            command=guardar,
            width=16
        ).grid(
            row=1,
            column=4,
            padx=15,
            pady=2
        )


        # Botón para modificar.

        tk.Button(
            self.pestana,
            text="Modificar Cliente",
            command=modificar,
            width=16
        ).grid(
            row=2,
            column=4,
            padx=15,
            pady=2
        )


        # Botón para eliminar.

        tk.Button(
            self.pestana,
            text="Eliminar Cliente",
            command=eliminar,
            width=16
        ).grid(
            row=3,
            column=4,
            padx=15,
            pady=2
        )


# ==============================================================================
# FIN DE CLIENTES.PY
# ==============================================================================

# CAMBIO ARQUITECTÓNICO FINAL
# ------------------------------------------------------------------------------
#
# Este archivo NO contiene:
#
#     tk.Tk()
#
# porque no crea la ventana principal.
#
# Tampoco contiene:
#
#     ttk.Notebook(...)
#
# porque no crea el Notebook.
#
# Tampoco contiene:
#
#     mainloop()
#
# porque el ciclo principal de Tkinter pertenece a interfaz.py.
#
# La responsabilidad de este módulo es:
#
#     RECIBIR UNA PESTAÑA
#             ↓
#     CONSTRUIR SU CONTENIDO
#             ↓
#     ADMINISTRAR SUS OPERACIONES CRUD
#
# La responsabilidad de interfaz.py es:
#
#     CREAR VENTANA
#             ↓
#     CREAR NOTEBOOK
#             ↓
#     CREAR LAS CINCO PESTAÑAS
#             ↓
#     ENTREGAR CADA PESTAÑA A SU CLASE
#
# Por eso la llamada desde interfaz.py será:
#
#     Clientes(pestana_clientes)
#
# y NO:
#
#     crear_pestana_clientes(notebook)