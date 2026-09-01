from user_admin import Admin

# Create the admin account instance
site_admin = Admin("Chris", "Victor", "Chidinma")

# Call the method to confirm it works
site_admin.privileges.show_privileges()
