import frappe

@frappe.whitelist()
def get_cached_data():
    cached_data = frappe.cache().get_value("cached_data")
    if cached_data:
        return cached_data
    else:
        data = fetch_data_from_database()
        frappe.cache().set_value("cached_data", data)
        return data
def fetch_data_from_database():
    items = frappe.get_all("User", fields=["email", "first_name"])
    formatted_data = []
    for item in items:
        formatted_data.append({
            "email":item.email,
            "first_name":item.first_name
        })
    return formatted_data