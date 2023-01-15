import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import tkinter as tk
root = tk.Tk()
root['bg'] = '#9E5D5D'
root.iconbitmap("krv.ico")
root.geometry("400x250")
root.title('Sustav Banke Krvi')



id_label = tk.Label(root, text="ID:", font=('Times New Roman', 16), bg='#28464B', fg='white', width=15)
id_entry = tk.Entry(root, font=('Times New Roman', 16), bg='white', fg='black')
id_label.grid(row=0, column=0, pady=10, padx=10, sticky='n')
id_entry.grid(row=1, column=0, pady=10, padx=10)


def login():
    user_id = id_entry.get()

    conn = pymysql.connect(host="localhost", user="root", password="root", database="baza_banke_krvi")
    cursor = conn.cursor()

    
    cursor.execute("SELECT * FROM zaposlenik WHERE id=%s", (user_id))
    result = cursor.fetchone()

    if result:
        
        print("Dobrodošli: ", user_id)
      
        main_menu = tk.Menu(root)
        root.config(menu=main_menu)

        
        admin_menu = tk.Menu(main_menu)

        ovlastima_menu = tk.Menu(main_menu)
        zaposlenik_menu = tk.Menu(main_menu)

        if user_id == '1':
            admin_window = tk.Menu(main_menu)

            def open_gui(option):
                if option == "Bolnica":
                    import CrudeBolnica
                    CrudeBolnica.gui(admin_window)
                    
                elif option == "Zaposlenik":
                    import CrudeZaposlenik
                    CrudeZaposlenik.gui(admin_window)
                    
                elif option == "Prijevoznik":
                    import PrijevoznikCrude
                    PrijevoznikCrude.gui(admin_window)
                    
                elif option == "Darivatelj":
                    import DarivateljCrude
                    DarivateljCrude.gui(admin_window)
                    
            option = tk.StringVar()
            admin_menu = tk.Menu(main_menu)
            main_menu.add_cascade(label="Admin", menu=admin_menu)
            admin_menu.add_radiobutton(label="Bolnica", variable=option, value="Bolnica", command=lambda: open_gui(option.get()))
            admin_menu.add_radiobutton(label="Zaposlenik", variable=option, value="Zaposlenik", command=lambda: open_gui(option.get()))
            admin_menu.add_radiobutton(label="Prijevoznik", variable=option, value="Prijevoznik", command=lambda: open_gui(option.get()))
            admin_menu.add_radiobutton(label="Darivatelj", variable=option, value="Darivatelj", command=lambda: open_gui(option.get()))
        
       #----------------------------------------------------------------------------------------------------------------------------
       
       
       
       
        elif 2 <= int(user_id) <= 10:
            zaposlenik_s_ovlastima_window = Toplevel(root)
            zaposlenik_s_ovlastima_window.geometry("600x600")
            ovlastima_menu = tk.Menu(main_menu)
            zaposlenik_s_ovlastima_window.destroy()
            main_menu.add_cascade(label="Zaposlenik s ovlastima",menu=ovlastima_menu)
            def open_gui_s_ovlastima(option):

                if option == "Bolnica":
                    import CrudeBolnicaZaposlenikSaOvlastima
                    CrudeBolnicaZaposlenikSaOvlastima.gui()
                elif option == "Zaposlenik":
                    import CrudeZaposlenikZaposlenikSaOvlastima
                    CrudeZaposlenikZaposlenikSaOvlastima.gui()
                elif option == "Prijevoznik":
                    import CrudePrijevoznikZaposlenikSaOvlastima
                    CrudePrijevoznikZaposlenikSaOvlastima.gui()
                elif option == "Darivatelj":
                    import CrudeDarivateljZaposlenikSaOvlastima
                    CrudeDarivateljZaposlenikSaOvlastima.gui()
                    
            option = tk.StringVar()
            ovlastima_menu.add_radiobutton(label="Bolnica", variable=option, value="Bolnica", command=lambda: open_gui_s_ovlastima(option.get()))
            ovlastima_menu.add_radiobutton(label="Zaposlenik", variable=option, value="Zaposlenik", command=lambda: open_gui_s_ovlastima(option.get()))
            ovlastima_menu.add_radiobutton(label="Prijevoznik", variable=option, value="Prijevoznik", command=lambda: open_gui_s_ovlastima(option.get()))
            ovlastima_menu.add_radiobutton(label="Darivatelj", variable=option, value="Darivatelj", command=lambda: open_gui_s_ovlastima(option.get()))
        
        
        #-----------------------------------------------------------------------------------------------------------------------
        
        

        if 11 <= int(user_id) <= 35:
            zaposlenik_window = Toplevel(root)
            zaposlenik_window.geometry("600x600")
            zaposlenik_menu = tk.Menu(main_menu)
            main_menu.add_cascade(label="Zaposlenik",menu=zaposlenik_menu)
            zaposlenik_window.destroy()
            def open_gui_zaposlenik(option):
                #Dodaj jos opcija i promjeni importove
                if option == "Bolnica":
                    import CrudeBolnicaObicanZaposlenik
                    CrudeBolnicaObicanZaposlenik.gui()
                elif option == "Zaposlenik":
                    import CrudeZaposlenikObicanZaposlenik
                    CrudeZaposlenikObicanZaposlenik.gui()
                elif option == "Prijevoznik":
                    import CrudePrijevoznikObicanZaposlenik
                    CrudePrijevoznikObicanZaposlenik.gui()
                elif option == "Darivatelj":
                    import CrudeDarivateljObicanZaposlenik
                    CrudeDarivateljObicanZaposlenik.gui()
            
            option = tk.StringVar()
            zaposlenik_menu.add_radiobutton(label="Bolnica", variable=option, value="Bolnica", command=lambda: open_gui_zaposlenik(option.get()))
            zaposlenik_menu.add_radiobutton(label="Zaposlenik", variable=option, value="Zaposlenik", command=lambda: open_gui_zaposlenik(option.get()))
            zaposlenik_menu.add_radiobutton(label="Prijevoznik", variable=option, value="Prijevoznik", command=lambda: open_gui_zaposlenik(option.get()))
            zaposlenik_menu.add_radiobutton(label="Darivatelj", variable=option, value="Darivatelj", command=lambda: open_gui_zaposlenik(option.get()))
        else:
            zaposlenik_window.withdraw()
        
        
    else:
        
        print("Pogrešan ID")

    cursor.close()
    conn.close()
login_button = tk.Button(root, text="Prijava", command=login, font=('Times New Roman', 16), bg='#28464B', fg='white')
login_button.grid(row=2, column=0, pady=10, padx=170, sticky='s')



root.mainloop()