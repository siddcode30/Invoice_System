from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")
invoice_list = [[2, "pen", 0.5, 1],
                [1, "notebook", 2, 4]]

doc.render({"name":"Siddhi",
            "phone":"555-555", 
            "invoice_list": invoice_list,
            "subtotal": 10,
            "salestax": "10%",
            "total": 9
            })
doc.save("new_invoice.docx")
