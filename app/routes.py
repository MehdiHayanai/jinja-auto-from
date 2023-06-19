from flask import render_template, url_for, flash, redirect, request
from app import app


@app.route("/", methods=["GET"])
def home():
    # Logic for generating the form
    form_fields = [
        {
            "id": "text_field",
            "name": "text_field",
            "type": "text",
            "label": "Text Field",
            "group_label": "Field Group 1",
            "placeholder": "Enter text",
            "required": True,
            "autocomplete": "off",
        },
        {
            "id": "float_field",
            "name": "float_field",
            "type": "number",
            "label": "Float Field",
            "group_label": "Field Group wow",
            "required": True,
            "step": "any",
        },
        {
            "id": "text_field2",
            "name": "text_field",
            "type": "text",
            "label": "Text Field",
            "group_label": "Field Group 1",
            "placeholder": "Enter text",
            "required": True,
            "autocomplete": "off",
        },
        {
            "id": "password_field",
            "name": "password_field",
            "type": "password",
            "label": "Password Field",
            "group_label": "Field Group 1",
            "required": True,
            "autocomplete": "new-password",
        },
        {
            "id": "email_field",
            "name": "email_field",
            "type": "email",
            "label": "Email Field",
            "group_label": "Field Group 2",
            "required": True,
            "autocomplete": "email",
        },
        {
            "id": "number_field",
            "name": "number_field",
            "type": "number",
            "label": "Number Field",
            "group_label": "Field Group 2",
            "min": 0,
            "max": 100,
            "step": 1,
        },
        {
            "id": "checkbox_field",
            "name": "checkbox_field",
            "type": "checkbox",
            "label": "Checkbox Field",
            "group_label": "Field Group 3",
            "options": [
                {"label": "Option 1", "value": "option1"},
                {"label": "Option 2", "value": "option2"},
                {"label": "Option 3", "value": "option3"},
            ],
        },
        {
            "id": "radio_field",
            "name": "radio_field",
            "type": "radio",
            "label": "Radio Button Field",
            "group_label": "Field Group 3",
            "options": [
                {"label": "Option 1", "value": "option1"},
                {"label": "Option 2", "value": "option2"},
                {"label": "Option 3", "value": "option3"},
            ],
        },
        {
            "id": "select_field",
            "name": "select_field",
            "type": "select",
            "label": "Select Field",
            "group_label": "Field Group 4",
            "options": [
                {"label": "Option 1", "value": "option1"},
                {"label": "Option 2", "value": "option2"},
                {"label": "Option 3", "value": "option3"},
            ],
        },
        {
            "id": "textarea_field",
            "name": "textarea_field",
            "type": "textarea",
            "label": "Textarea Field",
            "group_label": "Field Group 4",
            "rows": 4,
            "cols": 50,
        },
        {
            "id": "file_field",
            "name": "file_field",
            "type": "file",
            "label": "File Upload Field",
            "group_label": "Field Group 5",
        },
        {
            "id": "date_field",
            "name": "date_field",
            "type": "date",
            "label": "Date Field",
            "group_label": "Field Group 5",
        },
        {
            "id": "time_field",
            "name": "time_field",
            "type": "time",
            "label": "Time Field",
            "group_label": "Field Group 6",
        },
        {
            "id": "color_field",
            "name": "color_field",
            "type": "color",
            "label": "Color Field",
            # "group_label": "Field Group 6",
        },
    ]

    return render_template("index.html", form_fields=form_fields)
