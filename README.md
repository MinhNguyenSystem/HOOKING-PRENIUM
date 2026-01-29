# HOOKING-PRENIUM

Các tính năng chính như Hooking, Deobfuscate, Request Mocking và EXE Unpacking.

🪝 HookLibrary (PREMIUM)

Công cụ Reverse Engineering, Hooking API và Deobfuscate Python mạnh mẽ.

Copyright: MinhNguyen2412 & KhanhNguyen9872

HookLibrary là một framework tất cả-trong-một (All-in-One) dành cho các nhà phát triển và nghiên cứu bảo mật Python. Công cụ này cho phép can thiệp động (Dynamic Hooking) vào các hàm nội tại (Built-in functions), giải mã code bị làm rối (Deobfuscate), chặn bắt và chỉnh sửa request mạng, cũng như giải nén các file EXE được đóng gói bằng PyInstaller.

🚀 Tính Năng Nổi Bật
1. 🛠️ Dynamic Hooking & Dumping

Can thiệp và trích xuất dữ liệu từ các hàm quan trọng trong thời gian thực (Runtime):

Core Functions: Hook exec, eval, compile, builtins.type.

Serialization/Compression: Hook marshal.loads, zlib.decompress, binascii.unhexlify.

Security: Hook hashlib.md5.

Cơ chế: Tự động lưu (dump) mã nguồn đã giải mã ra thư mục HOOKING/ để phân tích.

2. 🧩 Deobfuscator (Trình giải mã tự động)

Hỗ trợ tự động phát hiện và giải mã nhiều loại obfuscator phổ biến hiện nay:

✅ Hyperion (V2, Custom Vars)

✅ Kramer

✅ Specter

✅ Impostor

✅ Berserker

✅ PyObfuscate

✅ AST-based Obfuscation

✅ Zlib Wrapper Detection

3. 🌐 Requests Interception & Mocking (REMOCK)

Một tính năng mạnh mẽ cho phép phân tích traffic mạng mà không cần cài đặt Proxy (như Burp Suite):

Logging: Xem toàn bộ URL, Headers, Body, JSON, Params của các request (GET, POST, PUT, DELETE...).

Mocking (Fake Response): Cho phép làm giả phản hồi từ server (Response Manipulation). Bạn có thể định nghĩa URL đích và dữ liệu trả về giả mạo để bypass các check server-side.

Telebot Detector: Tự động phát hiện và chặn các request gửi đến API Telegram (thường dùng trong botnet/stealer).

4. 📦 PyInstaller Extractor

Tự động phát hiện file .exe (đóng gói bằng PyInstaller).

Giải nén (Unpack) để lấy lại mã nguồn .pyc và các resource bên trong.

Hỗ trợ khôi phục header cho file .pyc.

5. 🛡️ Anti-Detection Bypass

Tích hợp sẵn các lớp giả lập (FakeFrame, bypass_layer) để qua mặt các cơ chế chống debug/hooking kiểm tra inspect.stack hoặc traceback.

⚙️ Cài Đặt

Công cụ tự động cài đặt các thư viện cần thiết khi khởi chạy. Tuy nhiên, bạn nên chuẩn bị môi trường Python 3.x.

Thư viện yêu cầu:

pip install rich colorama requests autopep8 pycryptodome

(Lưu ý: pycryptodome cần thiết cho module giải mã AES)

📖 Hướng Dẫn Sử Dụng

Khởi chạy công cụ bằng lệnh:

python hook.py

1. [START HOOK (FILE)]  : Chạy và Hook một file Python (.py, .pyc) hoặc giải nén .exe
2. [START HOOK (SHELL)] : Mở môi trường Shell tương tác đã được cài đặt Hook sẵn.
3. [SETTINGS HOOK]      : Bật/Tắt các module Hook cụ thể.
Chế độ xử lý File (Sau khi chọn File)

[R] REMOCKING AND HOOK: Chạy file và kích hoạt chế độ chặn bắt/sửa đổi Request mạng.

[D] DEOBF ENC NOT HOOK: Chỉ thực hiện giải mã (Deobfuscate) tĩnh và lưu code sạch, không chạy code.

[C] CONVERT PYC AND HOOK: Chuyển đổi version Magic Number của file .pyc (Python3x) và chạy.

[H] AUTO HOOKING: Chế độ chạy mặc định, tự động Hook tất cả các hàm đã cấu hình.

🕹️ Cấu Hình Nâng Cao (Settings)

Trong menu Settings, bạn có thể tùy chỉnh:

Bật/Tắt hook cho từng hàm riêng biệt (ví dụ: chỉ hook exec, tắt marshal).

Add Custom Function: Thêm bất kỳ hàm nào thuộc builtins hoặc thư viện đã import vào danh sách Hook (VD: thêm hook cho base64.b64decode).

View Modes:

3:dis: Tự động Disassemble (dịch ngược ra opcode) khi hook được marshal.

8:view: Hiển thị code đã giải mã ngay trên màn hình Terminal (sử dụng rich syntax highlighting).

⚠️ Lưu Ý Quan Trọng

Môi trường: Tool hoạt động tốt nhất trên Linux và Windows. Một số tính năng Remock nâng cao (Signal Handling) chỉ hỗ trợ Linux.
Vẫn còn khá nhiều bug chưa có time update nhưng đại khái là vẫn ổn!

An toàn: Khi chạy chế độ Hook, mã nguồn mục tiêu SẼ ĐƯỢC THỰC THI. Hãy cẩn thận khi phân tích malware, nên chạy trong máy ảo (VM) hoặc Sandbox.

©Copyright-Tool: MinhNguyen2412 and KhanhNguyen9872.

📞 Liên Hệ / Credits

Author: MinhNguyen2412

Co-Author: KhanhNguyen9872

Tool: HookLibrary (PREMIUM)

