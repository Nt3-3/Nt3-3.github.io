# INTRODUCCIÓN A PYGAME - EJEMPLO BÁSICO
# Este programa muestra los conceptos fundamentales de pygame
import pygame
import sys
# 1. INICIALIZACIÓN - SIEMPRE ES EL PRIMER PASO
pygame.init()
# 2. CONFIGURACIÓN DE LA VENTANA
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Primera Ventana con Pygame")
# 3. DEFINIR COLORES (RGB - Red, Green, Blue)
# Cada color va de 0 a 255
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
# 4. CONFIGURAR FUENTE PARA TEXTO
fuente = pygame.font.Font(None, 36)
# 5. CONTROLAR LA VELOCIDAD DEL JUEGO
reloj = pygame.time.Clock()
FPS = 60 # Frames por segundo
# 6. VARIABLES DEL PROGRAMA
pos_x = 50 # Posición X de nuestro círculo
pos_y = 200 # Posición Y de nuestro círculo
velocidad = 3 # Qué tan rápido se mueve
direccion = 1 # 1 = derecha, -1 = izquierda
contador_clicks = 0
def dibujar_todo():
    """Función que dibuja todo en la pantalla"""
    # Limpiar pantalla con color de fondo
    pantalla.fill(BLANCO)
    # Dibujar un círculo que se mueve
    pygame.draw.circle(pantalla, ROJO, (int(pos_x), int(pos_y)), 30)
    # Dibujar un rectángulo fijo
    pygame.draw.rect(pantalla, VERDE, (250, 100, 100, 50))
    # Dibujar una línea
    pygame.draw.line(pantalla, AZUL, (0, 300), (ANCHO, 300), 5)
# Mostrar texto
texto = fuente.render(f"Clicks: {contador_clicks}", True, NEGRO)
pantalla.blit(texto, (10, 10))
# Instrucciones
instruccion = pygame.font.Font(None, 24).render("Presiona ESPACIO para cambiar color", True, NEGRO)
pantalla.blit(instruccion, (10, ALTO - 30))
def manejar_eventos():
    """Función que maneja todos los eventos (teclado, mouse, etc.)"""
    global contador_clicks
    for evento in pygame.event.get():
        # El usuario cerró la ventana
        if evento.type() == pygame.QUIT:
            return False
        # El usuario presionó una tecla
        elif evento.type() == pygame.KEYDOWN:
            if evento.key() == pygame.K_SPACE:
                print("¡Presionaste ESPACIO!")
        elif evento.key() == pygame.K_ESCAPE:
            return False
        # El usuario hizo click con el mouse
        if evento.type() == pygame.MOUSEBUTTONDOWN:
            contador_clicks += 1
            print(f"Click en posición: {evento.pos}")
            return True # Continuar ejecutando
def actualizar_logica():
    """Función que actualiza la lógica del programa"""
    global pos_x, direccion
    # Mover el círculo
    pos_x += velocidad * direccion
    # Rebotar en los bordes
    if pos_x >= ANCHO - 30: # Borde derecho
        direccion = -1
    elif pos_x <= 30: # Borde izquierdo
        direccion = 1
def main():
    """Función principal del programa"""
    ejecutando = True
    print("=== BIENVENIDO A PYGAME ===")
    print("- Haz click en cualquier lugar")
    print("- Presiona ESPACIO")
    print("- Presiona ESC para salir")
    print("- El círculo rojo se mueve solo")
    # BUCLE PRINCIPAL DEL JUEGO
    while ejecutando:
        # 1. MANEJAR EVENTOS (input del usuario)
        ejecutando = manejar_eventos()
        # 2. ACTUALIZAR LÓGICA (movimiento, cálculos)
        actualizar_logica()
        # 3. DIBUJAR TODO EN PANTALLA
        dibujar_todo()
        # 4. ACTUALIZAR LA PANTALLA (mostrar cambios)
        pygame.display.flip()
        # 5. CONTROLAR VELOCIDAD
        reloj.tick(FPS)
        # Cerrar pygame correctamente
        pygame.quit()
        sys.exit()
# EJECUTAR EL PROGRAMA
if __name__ == "__main__":
    main()

"""
=== CONCEPTOS CLAVE DE PYGAME MOSTRADOS AQUÍ ===
1. INICIALIZACIÓN:
- pygame.init() - Inicializa todos los módulos
- pygame.display.set_mode() - Crea la ventana
2. COLORES:
- Se definen como tuplas RGB: (rojo, verde, azul)
- Valores de 0 a 255 para cada componente

3. DIBUJO:
- pygame.draw.circle() - Dibuja círculos
- pygame.draw.rect() - Dibuja rectángulos
- pygame.draw.line() - Dibuja líneas
- pantalla.fill() - Llena toda la pantalla con un color
4. TEXTO:
- pygame.font.Font() - Crea una fuente
- fuente.render() - Convierte texto en imagen
- pantalla.blit() - Pone la imagen en pantalla
5. EVENTOS:
- pygame.event.get() - Obtiene todos los eventos
- QUIT - Usuario cerró ventana
- KEYDOWN - Usuario presionó tecla
- MOUSEBUTTONDOWN - Usuario hizo click
6. BUCLE PRINCIPAL:
- Eventos → Lógica → Dibujo → Actualizar → Repetir
- pygame.display.flip() - Muestra lo dibujado
- reloj.tick(FPS) - Controla velocidad
7. COORDENADAS:
- (0,0) está en la esquina superior izquierda
- X aumenta hacia la derecha
- Y aumenta hacia abajo
"""