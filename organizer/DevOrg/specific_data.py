class SpecificFieldsToShow:
    db_devices_fields_names_to_show = [
        "Name",
        "Type",
        "Device friendly name",
        "Description",
        "Serial number",
        "Bought date",
        "Warranty type"
    ]
    db_date_field = "Bought date"
    db_option_type_field = [
        "Type",
        "Warranty type"
    ]
    # Displayed in HTML / Db column name / boolean show status
    db_devices_fields = [
        ["Name", "device_name", True],
        ["Type", "device_type", True],
        ["Device friendly name", "device_displayed_name", True],
        ["Description", "device_description", True],
        ["Serial number", "device_serial_number", True],
        ["Add date", "device_add_date", False],
        ["Bought date", "device_bought_date", True],
        ["Warranty type", "device_warranty", True],
        ["User", "user_connected", False]
    ]

    def check_display_bool(self):
        display_array = []
        for inner_array in self.db_devices_fields:
            if inner_array[2]:
                display_array.append(inner_array[0])
        return display_array

    def return_devices_fields_names_to_show(self):
        data = SpecificFieldsToShow.check_display_bool(self)
        return data

    def return_date_field_names(self):
        return self.db_date_field

    def return_type_option_field_name(self):
        return self.db_option_type_field[0]

    def return_warranty_option_field_name(self):
        return self.db_option_type_field[1]
