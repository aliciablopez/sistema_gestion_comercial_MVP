# ==============================================================================
# FACTURACION.PY
# MÓDULO DE LA PESTAÑA "FACTURACIÓN"
# ==============================================================================


# ==============================================================================
# 1. IMPORTACIONES
# ==============================================================================

# tkinter proporciona los elementos básicos de la interfaz gráfica:
# Label, Entry y Button.
import tkinter as tk

# ttk proporciona widgets adicionales de Tkinter.
# En este módulo utilizamos Treeview para mostrar las facturas.
from tkinter import ttk

# messagebox permite mostrar mensajes al usuario:
# errores, advertencias, información y confirmaciones.
from tkinter import messagebox


# ==============================================================================
# 2. CLASE / PESTAÑA
# ==============================================================================

# interfaz.py ya creó:
#
#   - la ventana principal
#   - el Notebook
#   - la pestaña correspondiente a Facturación
#
# Por eso este módulo NO crea otra ventana Tk().
#
# Recibimos la pestaña que ya existe.

class Facturacion:

    def __init__(self, pestana):

        # Guardamos la referencia a la pestaña.
        #
        # self representa la instancia actual de Facturacion.
        #
        # self.pestana permite que los métodos y funciones internas
        # trabajen posteriormente sobre esta misma pestaña.

        self.pestana = pestana


        # ==========================================================================
        # 3. FORMULARIO DE FACTURACIÓN
        # ==========================================================================

        # --------------------------------------------------------------------------
        # NÚMERO DE FACTURA
        # --------------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="N.º de factura:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_numero = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_numero.grid(
            row=0,
            column=1,
            padx=5,
            pady=4
        )


        # --------------------------------------------------------------------------
        # CLIENTE
        # --------------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="Cliente:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_cliente = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_cliente.grid(
            row=1,
            column=1,
            padx=5,
            pady=4
        )


        # --------------------------------------------------------------------------
        # TOTAL
        # --------------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="Total:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_total = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_total.grid(
            row=2,
            column=1,
            padx=5,
            pady=4
        )


        # ==========================================================================
        # 4. TREEVIEW
        # ==========================================================================

        # Treeview representa las facturas que fueron cargadas.
        #
        # El formulario (Entry) permite introducir datos.
        #
        # Treeview permite visualizar los registros.

        columnas = (
            "N.º de factura",
            "Cliente",
            "Total"
        )

        self.tabla = ttk.Treeview(
            self.pestana,
            columns=columnas,
            show="headings",
            height=10
        )


        # Ancho de cada columna.

        anchos = [180, 250, 150]


        # Configuramos los encabezados y las columnas.

        for idx, col in enumerate(columnas):

            self.tabla.heading(
                col,
                text=col
            )

            self.tabla.column(
                col,
                width=anchos[idx],
                anchor="center"
            )


        # Colocamos el Treeview debajo del formulario.

        self.tabla.grid(
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

        # --------------------------------------------------------------------------
        # LIMPIAR CAMPOS
        # --------------------------------------------------------------------------

        def limpiar_campos():

            # delete(0, tk.END) elimina todo el contenido
            # de cada Entry.

            self.caja_numero.delete(
                0,
                tk.END
            )

            self.caja_cliente.delete(
                0,
                tk.END
            )

            self.caja_total.delete(
                0,
                tk.END
            )


        # --------------------------------------------------------------------------
        # NUEVA FACTURA
        # --------------------------------------------------------------------------

        def nueva_factura():

            # Preparamos el formulario para introducir
            # una nueva factura.

            limpiar_campos()

            # Quitamos cualquier selección existente.

            self.tabla.selection_remove(
                self.tabla.selection()
            )

            # Colocamos el cursor en el primer campo.

            self.caja_numero.focus()


        # --------------------------------------------------------------------------
        # CARGAR DATOS DE LA FILA SELECCIONADA
        # --------------------------------------------------------------------------

        def cargar_datos_seleccionados(event=None):

            # Obtenemos la selección actual.

            seleccion = self.tabla.selection()

            if not seleccion:
                return


            # Obtenemos el identificador de la fila seleccionada.

            item_id = seleccion[0]


            # Recuperamos los valores almacenados en esa fila.

            valores = self.tabla.item(
                item_id,
                "values"
            )


            # Limpiamos los Entry antes de cargar los datos.

            limpiar_campos()


            # Pasamos los valores del Treeview al formulario.

            self.caja_numero.insert(
                0,
                valores[0]
            )

            self.caja_cliente.insert(
                0,
                valores[1]
            )

            self.caja_total.insert(
                0,
                valores[2]
            )


        # --------------------------------------------------------------------------
        # GUARDAR FACTURA
        # --------------------------------------------------------------------------

        def guardar():

            # Obtenemos los datos introducidos.

            numero = self.caja_numero.get().strip()
            cliente = self.caja_cliente.get().strip()
            total = self.caja_total.get().strip()


            # ----------------------------------------------------------------------
            # VALIDACIÓN
            # ----------------------------------------------------------------------

            # Número de factura y cliente son obligatorios.

            if not numero or not cliente:

                messagebox.showerror(
                    "Error",
                    "Número de factura y cliente son obligatorios.",
                    parent=self.pestana
                )

                return


            # Para este ejercicio comprobamos simplemente
            # que el número de factura contenga números.

            if not numero.isdigit():

                messagebox.showerror(
                    "Error",
                    "El número de factura debe contener solamente números.",
                    parent=self.pestana
                )

                return


            # ----------------------------------------------------------------------
            # CONTROL DE FACTURA DUPLICADA
            # ----------------------------------------------------------------------

            # Recorremos las facturas existentes.

            for item in self.tabla.get_children():

                valores = self.tabla.item(
                    item,
                    "values"
                )

                # La posición 0 corresponde al número de factura.

                if valores[0] == numero:

                    messagebox.showerror(
                        "Error",
                        "Ya existe una factura con ese número.",
                        parent=self.pestana
                    )

                    return


            # ----------------------------------------------------------------------
            # INSERTAR FACTURA
            # ----------------------------------------------------------------------

            self.tabla.insert(
                "",
                "end",
                values=(
                    numero,
                    cliente,
                    total
                )
            )


            messagebox.showinfo(
                "Éxito",
                "Factura guardada.",
                parent=self.pestana
            )

            limpiar_campos()


        # --------------------------------------------------------------------------
        # MODIFICAR FACTURA
        # --------------------------------------------------------------------------

        def modificar():

            # Comprobamos si existe una factura seleccionada.

            seleccion = self.tabla.selection()

            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona una factura para modificar.",
                    parent=self.pestana
                )

                return


            # Identificamos la fila.

            item_id = seleccion[0]


            # Recuperamos sus datos.

            valores = self.tabla.item(
                item_id,
                "values"
            )


            # ==========================================================================
            # VENTANA DE EDICIÓN
            # ==========================================================================

            ventana_edicion = tk.Toplevel(
                self.pestana
            )

            ventana_edicion.title(
                "Modificar Factura"
            )

            ventana_edicion.geometry(
                "400x280"
            )

            ventana_edicion.resizable(
                False,
                False
            )


            # Asociamos la ventana de edición con la pestaña.

            ventana_edicion.transient(
                self.pestana
            )

            # La edición se realiza de forma modal.

            ventana_edicion.grab_set()


            # ----------------------------------------------------------------------
            # TÍTULO
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Modificar datos de la factura",
                font=("Arial", 12, "bold")
            ).pack(
                pady=(15, 10)
            )


            # ----------------------------------------------------------------------
            # NÚMERO DE FACTURA
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="N.º de factura:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_numero = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_numero.pack(
                padx=30,
                pady=(2, 8)
            )

            caja_edicion_numero.insert(
                0,
                valores[0]
            )


            # ----------------------------------------------------------------------
            # CLIENTE
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Cliente:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_cliente = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_cliente.pack(
                padx=30,
                pady=(2, 8)
            )

            caja_edicion_cliente.insert(
                0,
                valores[1]
            )


            # ----------------------------------------------------------------------
            # TOTAL
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Total:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_total = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_total.pack(
                padx=30,
                pady=(2, 12)
            )

            caja_edicion_total.insert(
                0,
                valores[2]
            )


            # ==========================================================================
            # GUARDAR MODIFICACIÓN
            # ==========================================================================

            # Esta función está anidada dentro de modificar().
            #
            # Su tarea es guardar los cambios realizados
            # en la ventana de edición.

            def guardar_modificacion():

                numero_mod = (
                    caja_edicion_numero.get().strip()
                )

                cliente_mod = (
                    caja_edicion_cliente.get().strip()
                )

                total_mod = (
                    caja_edicion_total.get().strip()
                )


                # Validamos los campos obligatorios.

                if not numero_mod or not cliente_mod:

                    messagebox.showerror(
                        "Error",
                        "Número de factura y cliente son obligatorios.",
                        parent=ventana_edicion
                    )

                    return


                # Validamos el número de factura.

                if not numero_mod.isdigit():

                    messagebox.showerror(
                        "Error",
                        "El número de factura debe contener solamente números.",
                        parent=ventana_edicion
                    )

                    return


                # ------------------------------------------------------------------
                # CONTROL DE DUPLICADOS
                # ------------------------------------------------------------------

                # Buscamos si el nuevo número ya pertenece
                # a otra factura.

                for item in self.tabla.get_children():

                    # No comparamos la fila consigo misma.

                    if item == item_id:
                        continue


                    valores_otro = self.tabla.item(
                        item,
                        "values"
                    )

                    if valores_otro[0] == numero_mod:

                        messagebox.showerror(
                            "Error",
                            "Ya existe otra factura con ese número.",
                            parent=ventana_edicion
                        )

                        return


                # ------------------------------------------------------------------
                # ACTUALIZAR LA FILA
                # ------------------------------------------------------------------

                nuevos_valores = (
                    numero_mod,
                    cliente_mod,
                    total_mod
                )


                self.tabla.item(
                    item_id,
                    values=nuevos_valores
                )


                # Cerramos la ventana de edición.

                ventana_edicion.destroy()


                messagebox.showinfo(
                    "Éxito",
                    "La factura fue modificada correctamente.",
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


            caja_edicion_numero.focus()


        # --------------------------------------------------------------------------
        # ELIMINAR FACTURA
        # --------------------------------------------------------------------------

        def eliminar():

            # Comprobamos si existe una selección.

            seleccion = self.tabla.selection()

            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona una factura para eliminar.",
                    parent=self.pestana
                )

                return


            # Obtenemos el identificador de la fila.

            item_id = seleccion[0]


            # Recuperamos los valores.

            valores = self.tabla.item(
                item_id,
                "values"
            )


            numero = valores[0]
            cliente = valores[1]
            total = valores[2]


            # ----------------------------------------------------------------------
            # CONFIRMACIÓN
            # ----------------------------------------------------------------------

            confirmar = messagebox.askyesno(
                "Confirmar baja",
                f"¿Deseas eliminar la siguiente factura?\n\n"
                f"N.º de factura: {numero}\n"
                f"Cliente: {cliente}\n"
                f"Total: {total}\n\n"
                f"Esta operación no se puede deshacer.",
                parent=self.pestana
            )


            if confirmar:

                # Eliminamos la fila seleccionada.

                self.tabla.delete(
                    item_id
                )

                limpiar_campos()


                messagebox.showinfo(
                    "Baja realizada",
                    "La factura fue eliminada correctamente.",
                    parent=self.pestana
                )


        # ==========================================================================
        # 6. ENLACE DE SELECCIÓN
        # ==========================================================================

        # El usuario selecciona una fila.
        #
        # La selección genera el evento:
        #
        #     <<TreeviewSelect>>
        #
        # bind() conecta ese evento con
        # cargar_datos_seleccionados().
        #
        # Por lo tanto:
        #
        #     seleccionar fila
        #           ↓
        #     evento
        #           ↓
        #     bind()
        #           ↓
        #     cargar_datos_seleccionados()
        #           ↓
        #     datos → Entry

        self.tabla.bind(
            "<<TreeviewSelect>>",
            cargar_datos_seleccionados
        )


        # ==========================================================================
        # 7. BOTONES CRUD
        # ==========================================================================

        tk.Button(
            self.pestana,
            text="Nueva factura",
            command=nueva_factura,
            width=16
        ).grid(
            row=0,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )


        tk.Button(
            self.pestana,
            text="Guardar factura",
            command=guardar,
            width=16
        ).grid(
            row=1,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )


        tk.Button(
            self.pestana,
            text="Modificar factura",
            command=modificar,
            width=16
        ).grid(
            row=2,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )


        tk.Button(
            self.pestana,
            text="Eliminar factura",
            command=eliminar,
            width=16
        ).grid(
            row=3,
            column=4,
            padx=15,
            pady=2,
            sticky="w"
        )


# ==============================================================================
# FIN DE FACTURACION.PY
# ==============================================================================

# Este módulo no crea una ventana Tk().
#
# Tampoco contiene mainloop().
#
# Su responsabilidad es construir y administrar
# el contenido de la pestaña de Facturación.