import qrcode
import image

qr = qrcode.QRCode(
    version=15,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=6
)
data = 'https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqblFFd0QzMkVFQ212RV9kMFQ3YkxxTzFHSTZud3xBQ3Jtc0trRDNJcTZ5THdPUmtrSVJmckVXMV83ZmZPdGpqQ2ZSeVJmOXlRcW01LWVvZW13LUFXTGFEZndZSEwxbnVUM01QX3Fzb3hEUXVfUWE1Z0xqRTNQaXB0UjAxZXEwNEF1d3d6MndWd19lY2IwWWVEemx4dw&q=https%3A%2F%2Fwww.facebook.com%2Ftechiecoder%2F%3Fhc_ref%3DARRyA6bdkrQEIUt3m_ZxYtYFjA02Qo1yscBsa5lCOQ8M8fH8NX6ikrjnUTPmur4TlYQ%26fref%3Dnf'
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color='black',back_color='white')
image.save = ('test.jpg')