import cv2

class picture:

    def __init__(self):
        pass
    
    def capturarImagem(self):
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        file = "picture.png"
        retval, img = camera.read()
        cv2.imshow('Foto',img)
        cv2.imwrite(file,img)
        cv2.destroyAllWindows()

    def exibirImagem(self):
        imagem = cv2.imread("picture.png")
        cv2.imshow("Sua Foto - JOGO DO BIXAO", imagem)

    def capturaExibe(self):
        self.capturarImagem()
        self.exibirImagem()
