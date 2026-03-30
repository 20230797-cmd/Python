import tkinter as tk
from tkinter import messagebox
import google.generativeai as genai
import threading

# Cau hinh API Key
API_KEY = "AIzaSyDxgJwiEUPUnjc9zmNNtXSqqvyILyEgClM"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('models/gemini-2.5-flash')

def fetch_code_from_api(user_prompt):
    try:
        # Tao prompt
        system_prompt = f"Viết code Python cho yêu cầu: '{user_prompt}'. Chỉ in ra code, không giải thích thêm."
        response = model.generate_content(system_prompt)
        
        # Loc bo ky tu markdown tra ve tu API
        result = response.text.replace("```python", "").replace("```", "").strip()
        
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, result)
        
    except Exception as e:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, f"Loi ket noi: {e}")
        
    finally:
        btn_generate.config(state=tk.NORMAL, text="TẠO CODE")

def handle_click():
    req = entry_request.get()
    
    if req.strip() == "":
        messagebox.showwarning("Thông báo", "Vui lòng nhập yêu cầu bài toán!")
        return
    
    # Block nut bam trong luc cho API phan hoi
    btn_generate.config(state=tk.DISABLED, text="Đang tải...")
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, "Đang kết nối API...")
    
    # Dung thread de GUI khong bi treo
    t = threading.Thread(target=fetch_code_from_api, args=(req,))
    t.start()

# --- GUI ---
root = tk.Tk()
root.title("Ứng dụng tạo Code Python")
root.geometry("650x550")
root.configure(bg="#f8f9fa")

lbl_title = tk.Label(root, text="CÔNG CỤ TẠO CODE PYTHON", font=("Segoe UI", 16, "bold"), bg="#f8f9fa", fg="#343a40")
lbl_title.pack(pady=(20, 10))

frame_input = tk.Frame(root, bg="#f8f9fa")
frame_input.pack(fill="x", padx=30)

lbl_req = tk.Label(frame_input, text="Nhập yêu cầu:", font=("Segoe UI", 10), bg="#f8f9fa")
lbl_req.pack(anchor="w")

entry_request = tk.Entry(frame_input, font=("Consolas", 12), relief="solid", bd=1)
entry_request.pack(fill="x", pady=5, ipady=5)
entry_request.insert(0, "Chương trình tính tổng từ 1 đến n")

btn_generate = tk.Button(root, text="TẠO CODE", command=handle_click, 
                         bg="#0d6efd", fg="white", font=("Segoe UI", 10, "bold"), 
                         relief="flat", cursor="hand2", padx=20, pady=8)
btn_generate.pack(pady=10)

lbl_res = tk.Label(root, text="Kết quả:", font=("Segoe UI", 10), bg="#f8f9fa")
lbl_res.pack(anchor="w", padx=30)

text_output = tk.Text(root, font=("Consolas", 11), bg="#212529", fg="#f8f9fa", 
                      insertbackground="white", relief="flat", padx=10, pady=10)
text_output.pack(expand=True, fill="both", padx=30, pady=(0, 10))

footer_text = "Phạm Gia Khánh | MSSV: 20230797 | DCCNTT14.2"
lbl_footer = tk.Label(root, text=footer_text, font=("Segoe UI", 9, "italic"), bg="#f8f9fa", fg="#6c757d")
lbl_footer.pack(pady=(0, 10))

root.mainloop()
