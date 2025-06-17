# HOOKING-PRENIUM
hooking library (móc, ghi đè thư viện-module)

# Chức năng

I) DEOBF (GIẢI MÃ THỦ CÔNG): Các dạng mã hóa thông thường, cơ bản (vd: specter, impostor, berseker, hyperion,...)
II) GHI ĐÈ, MÓC DỮ LIỆU TRỰC TIẾP THÔNG CÁC THƯ VIỆN
III) REMOCK (REQUESTS-MOCKING): Chia ra hai dạng
   - 1. ÁP DỤNG PHƯƠNG THỨC MÓC REQUESTS TRỰC TIẾP SAU ĐÓ DEBUG RA HOST - link, rồi tiến hành fake response để change yêu cầu
   - 2. Tương tự dạng 1 nhưng thay vào đó tránh trường hợp bị anti thì nó sẽ mod lại file (api.py) sau đó thực thi file main.py qua trung gian nó sẽ tránh được anti mà thk enc nó dựng ra
