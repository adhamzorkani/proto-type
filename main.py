import tkinter as tk 
from tkinter import messagebox
import folium
import webbrowser

class ParkingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking System")

        self.accounts = {}  # Dictionary to store username and password combinations

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.old_password = tk.StringVar()
        self.new_password = tk.StringVar()
        self.brand = tk.StringVar()
        self.make = tk.StringVar()
        self.model = tk.StringVar()

        self.login_frame = tk.Frame(self.root)
        self.create_account_frame = tk.Frame(self.root)
        self.home_frame = tk.Frame(self.root)
        self.edit_password_frame = tk.Frame(self.root)
        self.edit_car_details_frame = tk.Frame(self.root)

        self.show_login_create_buttons()

    def show_login_create_buttons(self):
        login_button = tk.Button(self.root, text="Login", command=self.show_login_frame)
        login_button.pack()

        create_account_button = tk.Button(self.root, text="Create Account", command=self.show_create_account_frame)
        create_account_button.pack()

    def show_login_frame(self):
        self.hide_frames()
        self.login_frame.pack()

        login_label = tk.Label(self.login_frame, text="Login")
        login_label.pack()

        username_label = tk.Label(self.login_frame, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(self.login_frame, textvariable=self.username)
        username_entry.pack()

        password_label = tk.Label(self.login_frame, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self.login_frame, textvariable=self.password, show="*")
        password_entry.pack()

        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.pack()

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if username in self.accounts and self.accounts[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.hide_frames()
            self.show_home_frame()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def show_create_account_frame(self):
        self.hide_frames()
        self.create_account_frame.pack()

        create_account_label = tk.Label(self.create_account_frame, text="Create Account")
        create_account_label.pack()

        username_label = tk.Label(self.create_account_frame, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(self.create_account_frame, textvariable=self.username)
        username_entry.pack()

        password_label = tk.Label(self.create_account_frame, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self.create_account_frame, textvariable=self.password, show="*")
        password_entry.pack()

        create_account_button = tk.Button(self.create_account_frame, text="Create Account", command=self.create_account)
        create_account_button.pack()

    def create_account(self):
        username = self.username.get()
        password = self.password.get()

        if username in self.accounts:
            messagebox.showerror("Error", "Username already exists!")
        else:
            self.accounts[username] = password
            messagebox.showinfo("Success", "Account created successfully!")

            self.hide_frames()
            self.show_edit_car_details_frame()

    def show_edit_car_details_frame(self):
        self.hide_frames()
        self.edit_car_details_frame.pack()

        edit_car_details_label = tk.Label(self.edit_car_details_frame, text="Edit Car Details")
        edit_car_details_label.pack()

        brand_label = tk.Label(self.edit_car_details_frame, text="Brand:")
        brand_label.pack()
        brand_entry = tk.Entry(self.edit_car_details_frame, textvariable=self.brand)
        brand_entry.pack()

        make_label = tk.Label(self.edit_car_details_frame, text="Make:")
        make_label.pack()
        make_entry = tk.Entry(self.edit_car_details_frame, textvariable=self.make)
        make_entry.pack()

        model_label = tk.Label(self.edit_car_details_frame, text="Model:")
        model_label.pack()
        model_entry = tk.Entry(self.edit_car_details_frame, textvariable=self.model)
        model_entry.pack()

        submit_button = tk.Button(self.edit_car_details_frame, text="Submit", command=self.submit_car_details)
        submit_button.pack()

    def submit_car_details(self):
        messagebox.showinfo("Success", "Car details updated successfully!")
        self.hide_frames()
        self.show_home_frame()

    def show_home_frame(self):
        self.hide_frames()
        self.home_frame.pack()

        self.edit_profile_button = tk.Button(self.home_frame, text="Edit Profile", command=self.show_edit_password_frame)
        self.edit_profile_button.pack()

        edit_car_details_button = tk.Button(self.home_frame, text="Edit Car Details", command=self.show_edit_car_details_frame)
        edit_car_details_button.pack()

        view_map_button = tk.Button(self.home_frame, text="View Map", command=self.view_map)
        view_map_button.pack()

    def show_edit_password_frame(self):
        self.hide_frames()
        self.edit_password_frame.pack()

        edit_password_label = tk.Label(self.edit_password_frame, text="Edit Password")
        edit_password_label.pack()

        old_password_label = tk.Label(self.edit_password_frame, text="Old Password:")
        old_password_label.pack()
        old_password_entry = tk.Entry(self.edit_password_frame, textvariable=self.old_password, show="*")
        old_password_entry.pack()

        new_password_label = tk.Label(self.edit_password_frame, text="New Password:")
        new_password_label.pack()
        new_password_entry = tk.Entry(self.edit_password_frame, textvariable=self.new_password, show="*")
        new_password_entry.pack()

        submit_button = tk.Button(self.edit_password_frame, text="Submit", command=self.submit_password)
        submit_button.pack()

    def submit_password(self):
        username = self.username.get()
        old_password = self.old_password.get()
        new_password = self.new_password.get()

        if username in self.accounts and self.accounts[username] == old_password:
            self.accounts[username] = new_password
            messagebox.showinfo("Success", "Password updated successfully!")
        else:
            messagebox.showerror("Error", "Invalid old password!")

        self.hide_frames()
        self.show_home_frame()

    def view_map(self):
        # Create a map using folium
        parking_map = folium.Map(location=[30.016682012062596, 31.50017742364378], zoom_start=25)
        
        # Add a marker for the parking location
        marker = folium.Marker(location=[30.016682012062596, 31.50017742364378], popup="Current Location")
        marker.add_to(parking_map)
        
        # Save the map as an HTML file
        parking_map.save("parking_map.html")
        
        # Open the map in a web browser
        webbrowser.open("parking_map.html")

    def hide_frames(self):
        self.login_frame.pack_forget()
        self.create_account_frame.pack_forget()
        self.home_frame.pack_forget()
        self.edit_password_frame.pack_forget()
        self.edit_car_details_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    parking_system = ParkingSystem(root)
    root.mainloop()
    
    