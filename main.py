import board
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# Organizando os pinos na ordem física que você definiu
pinos_id = [board.GP0, board.GP1, board.GP4, board.GP2, board.GP3]
botoes = []

for p in pinos_id:
    btn = digitalio.DigitalInOut(p)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    botoes.append(btn)

# Mapeamento de teclas
atalhos = [Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR, Keycode.FIVE]

print("🚀 MacroPad Otimizado - Pronto!")

while True:
    for i, botao in enumerate(botoes):
        if not botao.value:  # Botão pressionado (LOW)
            # Envia a combinação de forma mais segura
            kbd.send(Keycode.CONTROL, Keycode.ALT, atalhos[i])
            
            print(f"Atalho {i+1} enviado!")
            
            # --- MELHORIA AQUI: ESPERA SOLTAR ---
            # Enquanto o botão estiver pressionado, ele fica preso neste loop vazio
            # Isso evita que o comando seja enviado mil vezes se você segurar o botão
            while not botao.value:
                time.sleep(0.01) 
                
    time.sleep(0.01) # Small delay para poupar energia da CPU