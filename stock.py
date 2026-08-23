# ==============================================================================
# STOCK.PY
# MÓDULO DE LA PESTAÑA "STOCK"
# ==============================================================================


# ==============================================================================
# 1. IMPORTACIONES
# ==============================================================================

# tkinter proporciona los elementos básicos de la interfaz gráfica:
# ventanas, etiquetas, cajas de texto y botones.
import tkinter as tk

# ttk proporciona widgets adicionales de Tkinter.
# En este módulo utilizamos Treeview para mostrar los productos.
from tkinter import ttk

# messagebox permite mostrar mensajes de información,
# errores, advertencias y confirmaciones.
from tkinter import messagebox


# ==============================================================================
# 2. CLASE / PESTAÑA
# ==============================================================================

# interfaz.py ya creó la ventana principal y el Notebook.
#
# También creó la pestaña que corresponde a Stock.
#
# Por eso aquí NO creamos:
#
#     tk.Tk()
#     ttk.Notebook()
#
# La clase recibe la pestaña que ya existe.
#
# "pestana" es el parámetro que recibe la clase.
#
# self.pestana será la referencia que guardaremos para poder
# utilizar esa pestaña posteriormente desde los métodos de la clase.

class Stock:

    def __init__(self, pestana):

        # Guardamos la referencia de la pestaña.
        #
        # self representa la instancia actual de Stock.
        #
        # Gracias a self.pestana, los distintos métodos de esta instancia
        # podrán trabajar sobre la misma pestaña.

        self.pestana = pestana


        # ==========================================================================
        # 3. FORMULARIO DE STOCK
        # ==========================================================================

        # --------------------------------------------------------------------------
        # PRODUCTO
        # --------------------------------------------------------------------------

        # Label identifica qué dato debe introducir el usuario.

        tk.Label(
            self.pestana,
            text="Producto:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        # Entry es la caja donde el usuario introduce el nombre
        # del producto.

        self.caja_producto = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_producto.grid(
            row=0,
            column=1,
            padx=5,
            pady=4
        )


        # --------------------------------------------------------------------------
        # SKU
        # --------------------------------------------------------------------------

        # SKU (Stock Keeping Unit) identifica de manera única
        # un producto dentro del inventario.

        tk.Label(
            self.pestana,
            text="SKU:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_sku = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_sku.grid(
            row=1,
            column=1,
            padx=5,
            pady=4
        )


        # --------------------------------------------------------------------------
        # CANTIDAD
        # --------------------------------------------------------------------------

        tk.Label(
            self.pestana,
            text="Cantidad:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=4,
            sticky="e"
        )

        self.caja_cantidad = tk.Entry(
            self.pestana,
            width=25
        )

        self.caja_cantidad.grid(
            row=2,
            column=1,
            padx=5,
            pady=4
        )


        # ==========================================================================
        # 4. TREEVIEW
        # ==========================================================================

        # Treeview NO es el formulario.
        #
        # El formulario utiliza Entry para introducir datos.
        #
        # Treeview representa los registros que ya fueron cargados.

        columnas = (
            "Producto",
            "SKU",
            "Cantidad"
        )

        self.tabla = ttk.Treeview(
            self.pestana,
            columns=columnas,
            show="headings",
            height=10
        )


        # Ancho correspondiente a cada columna.

        anchos = [250, 150, 120]


        # Recorremos las columnas para configurar cada encabezado
        # y su ancho.

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

            # delete(0, tk.END) elimina el contenido completo del Entry.
            #
            # 0 representa la posición inicial.
            # tk.END representa el final del contenido.

            self.caja_producto.delete(0, tk.END)
            self.caja_sku.delete(0, tk.END)
            self.caja_cantidad.delete(0, tk.END)


        # --------------------------------------------------------------------------
        # NUEVO PRODUCTO
        # --------------------------------------------------------------------------

        def nuevo_producto():

            # Dejamos el formulario preparado para una nueva carga.

            limpiar_campos()

            # Quitamos la selección actual del Treeview.

            self.tabla.selection_remove(
                self.tabla.selection()
            )

            # Colocamos el cursor en el primer campo.

            self.caja_producto.focus()


        # --------------------------------------------------------------------------
        # CARGAR DATOS DE LA FILA SELECCIONADA
        # --------------------------------------------------------------------------

        def cargar_datos_seleccionados(event=None):

            # Preguntamos qué fila está seleccionada.

            seleccion = self.tabla.selection()

            # Si no hay ninguna selección, terminamos la función.

            if not seleccion:
                return


            # selection() devuelve los identificadores de las filas.
            #
            # [0] obtiene el identificador de la primera fila seleccionada.

            item_id = seleccion[0]


            # Recuperamos los valores almacenados en esa fila.

            valores = self.tabla.item(
                item_id,
                "values"
            )


            # Limpiamos el formulario antes de cargar los datos.

            limpiar_campos()


            # Llevamos los valores del Treeview nuevamente
            # hacia los Entry.

            self.caja_producto.insert(
                0,
                valores[0]
            )

            self.caja_sku.insert(
                0,
                valores[1]
            )

            self.caja_cantidad.insert(
                0,
                valores[2]
            )


        # --------------------------------------------------------------------------
        # GUARDAR PRODUCTO
        # --------------------------------------------------------------------------

        def guardar():

            # .get() obtiene el contenido actual de cada Entry.

            producto = self.caja_producto.get().strip()
            sku = self.caja_sku.get().strip()
            cantidad = self.caja_cantidad.get().strip()


            # ----------------------------------------------------------------------
            # VALIDACIÓN
            # ----------------------------------------------------------------------

            # Para este ejercicio nos interesa practicar la lógica de validación.
            #
            # Producto y SKU son obligatorios.

            if not producto or not sku:

                messagebox.showerror(
                    "Error",
                    "Producto y SKU son obligatorios.",
                    parent=self.pestana
                )

                return


            # La cantidad debe contener solamente números.

            if not cantidad.isdigit():

                messagebox.showerror(
                    "Error",
                    "La cantidad debe contener solamente números.",
                    parent=self.pestana
                )

                return


            # ----------------------------------------------------------------------
            # CONTROL DE SKU DUPLICADO
            # ----------------------------------------------------------------------

            # Recorremos las filas existentes.

            for item in self.tabla.get_children():

                valores = self.tabla.item(
                    item,
                    "values"
                )

                # La posición 1 corresponde al SKU.

                if valores[1] == sku:

                    messagebox.showerror(
                        "Error",
                        "Ya existe un producto con ese SKU.",
                        parent=self.pestana
                    )

                    return


            # ----------------------------------------------------------------------
            # INSERTAR REGISTRO
            # ----------------------------------------------------------------------

            # Insertamos una nueva fila en el Treeview.

            self.tabla.insert(
                "",
                "end",
                values=(
                    producto,
                    sku,
                    cantidad
                )
            )


            messagebox.showinfo(
                "Éxito",
                "Producto guardado.",
                parent=self.pestana
            )

            limpiar_campos()


        # --------------------------------------------------------------------------
        # MODIFICAR PRODUCTO
        # --------------------------------------------------------------------------

        def modificar():

            # Primero comprobamos que exista una fila seleccionada.

            seleccion = self.tabla.selection()

            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona un producto para modificar.",
                    parent=self.pestana
                )

                return


            # Identificamos la fila.

            item_id = seleccion[0]


            # Recuperamos sus valores actuales.

            valores = self.tabla.item(
                item_id,
                "values"
            )


            # ======================================================================
            # VENTANA DE EDICIÓN
            # ======================================================================

            # Creamos una ventana secundaria para modificar el registro.

            ventana_edicion = tk.Toplevel(
                self.pestana
            )

            ventana_edicion.title(
                "Modificar Producto"
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

            # grab_set() hace que el usuario deba terminar esta operación
            # antes de volver a utilizar la pestaña principal.

            ventana_edicion.grab_set()


            # ----------------------------------------------------------------------
            # CAMPOS DE EDICIÓN
            # ----------------------------------------------------------------------

            tk.Label(
                ventana_edicion,
                text="Modificar datos del producto",
                font=("Arial", 12, "bold")
            ).pack(
                pady=(15, 10)
            )


            tk.Label(
                ventana_edicion,
                text="Producto:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_producto = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_producto.pack(
                padx=30,
                pady=(2, 8)
            )

            caja_edicion_producto.insert(
                0,
                valores[0]
            )


            tk.Label(
                ventana_edicion,
                text="SKU:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_sku = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_sku.pack(
                padx=30,
                pady=(2, 8)
            )

            caja_edicion_sku.insert(
                0,
                valores[1]
            )


            tk.Label(
                ventana_edicion,
                text="Cantidad:"
            ).pack(
                anchor="w",
                padx=30
            )

            caja_edicion_cantidad = tk.Entry(
                ventana_edicion,
                width=40
            )

            caja_edicion_cantidad.pack(
                padx=30,
                pady=(2, 12)
            )

            caja_edicion_cantidad.insert(
                0,
                valores[2]
            )


            # ======================================================================
            # GUARDAR MODIFICACIÓN
            # ======================================================================

            # Esta función está dentro de modificar().
            #
            # Es una función anidada.
            #
            # Su función es encargarse exclusivamente de guardar
            # los cambios realizados en esta ventana de edición.

            def guardar_modificacion():

                producto_mod = (
                    caja_edicion_producto.get().strip()
                )

                sku_mod = (
                    caja_edicion_sku.get().strip()
                )

                cantidad_mod = (
                    caja_edicion_cantidad.get().strip()
                )


                # Validamos los campos obligatorios.

                if not producto_mod or not sku_mod:

                    messagebox.showerror(
                        "Error",
                        "Producto y SKU son obligatorios.",
                        parent=ventana_edicion
                    )

                    return


                # Validamos la cantidad.

                if not cantidad_mod.isdigit():

                    messagebox.showerror(
                        "Error",
                        "La cantidad debe contener solamente números.",
                        parent=ventana_edicion
                    )

                    return


                # Comprobamos que el SKU no pertenezca
                # a otro producto.

                for item in self.tabla.get_children():

                    # No debemos comparar la fila consigo misma.

                    if item == item_id:
                        continue


                    valores_otro = self.tabla.item(
                        item,
                        "values"
                    )

                    if valores_otro[1] == sku_mod:

                        messagebox.showerror(
                            "Error",
                            "Ya existe otro producto con ese SKU.",
                            parent=ventana_edicion
                        )

                        return


                # Construimos los nuevos valores.

                nuevos_valores = (
                    producto_mod,
                    sku_mod,
                    cantidad_mod
                )


                # Reemplazamos los valores de la fila.

                self.tabla.item(
                    item_id,
                    values=nuevos_valores
                )


                # Cerramos la ventana de edición.

                ventana_edicion.destroy()


                messagebox.showinfo(
                    "Éxito",
                    "El producto fue modificado correctamente.",
                    parent=self.pestana
                )


            # ----------------------------------------------------------------------
            # BOTONES DE LA VENTANA DE EDICIÓN
            # ----------------------------------------------------------------------

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


            caja_edicion_producto.focus()


        # --------------------------------------------------------------------------
        # ELIMINAR PRODUCTO
        # --------------------------------------------------------------------------

        def eliminar():

            seleccion = self.tabla.selection()

            if not seleccion:

                messagebox.showwarning(
                    "Atención",
                    "Selecciona un producto para eliminar.",
                    parent=self.pestana
                )

                return


            # Recuperamos el identificador de la fila.

            item_id = seleccion[0]


            # Recuperamos los valores.

            valores = self.tabla.item(
                item_id,
                "values"
            )


            producto = valores[0]
            sku = valores[1]
            cantidad = valores[2]


            # Pedimos confirmación antes de eliminar.

            confirmar = messagebox.askyesno(
                "Confirmar baja",
                f"¿Deseas eliminar el siguiente producto?\n\n"
                f"Producto: {producto}\n"
                f"SKU: {sku}\n"
                f"Cantidad: {cantidad}\n\n"
                f"Esta operación no se puede deshacer.",
                parent=self.pestana
            )


            if confirmar:

                # Eliminamos solamente la fila seleccionada.

                self.tabla.delete(
                    item_id
                )

                limpiar_campos()

                messagebox.showinfo(
                    "Baja realizada",
                    "El producto fue eliminado correctamente.",
                    parent=self.pestana
                )


        # ==========================================================================
        # 6. ENLACE DE SELECCIÓN
        # ==========================================================================

        # Cuando el usuario selecciona una fila del Treeview,
        # se produce el evento <<TreeviewSelect>>.
        #
        # bind() conecta ese evento con la función
        # cargar_datos_seleccionados().
        #
        # Es decir:
        #
        #     clic del usuario
        #          ↓
        #     selección de fila
        #          ↓
        #     evento TreeviewSelect
        #          ↓
        #     bind()
        #          ↓
        #     cargar_datos_seleccionados()
        #
        # El parámetro event=None permite que Tkinter
        # pueda pasarle automáticamente la información del evento.

        self.tabla.bind(
            "<<TreeviewSelect>>",
            cargar_datos_seleccionados
        )


        # ==========================================================================
        # 7. BOTONES CRUD
        # ==========================================================================

        tk.Button(
            self.pestana,
            text="Nuevo producto",
            command=nuevo_producto,
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
            text="Guardar producto",
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
            text="Modificar producto",
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
            text="Eliminar producto",
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
# FIN DE STOCK.PY
# ==============================================================================

# Este módulo NO contiene:
#
#     tk.Tk()
#     mainloop()
#
# porque esas responsabilidades pertenecen a main.py / interfaz.py.
#
# Stock solamente construye y administra el contenido de su propia pestaña.