from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# الأحرف المستخدمة حسب درجة السطوع
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # رمادي

def pixels_to_ascii(image):
    pixels = np.array(image).astype(int)
    ascii_str = ""
    for row in pixels:
        for pixel in row:
            ascii_str += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
        ascii_str += "\n"
    return ascii_str

def convert_image_to_ascii(path, new_width=100):
    try:
        image = Image.open(path)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open image:\n{e}")
        return ""

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_art = pixels_to_ascii(image)
    return ascii_art

# ========== واجهة رسومية بسيطة ==========
def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
    )
    if not file_path:
        return

    ascii_art = convert_image_to_ascii(file_path, new_width=100)
    if ascii_art:
        output.delete("1.0", tk.END)
        output.insert(tk.END, ascii_art)

        # حفظ الناتج في ملف
        with open("ascii_output.txt", "w", encoding="utf-8") as f:
            f.write(ascii_art)

        messagebox.showinfo("Success", "Image converted to ASCII and saved as ascii_output.txt")

# إعداد النافذة
root = tk.Tk()
root.title("Image to ASCII Art by Nalonary")
root.geometry("800x600")

btn = tk.Button(root, text="🖼️ اختر صورة", font=("Arial", 14), command=open_image)
btn.pack(pady=10)

output = tk.Text(root, bg="black", fg="white", font=("Courier", 6), wrap=tk.NONE)
output.pack(expand=True, fill="both")

root.mainloop()
# تم إنشاء هذا البرنامج لتحويل الصور إلى فن ASCII باستخدام مكتبة PIL وTkinter
# تأكد من تثبيت المكتبات المطلوبة باستخدام: