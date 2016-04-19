#Realizado por: Diego Lozano , Ximena Medina, Ivan Herrera

#   En la carpeta se encuentran tres archivos de audio con los cuales se prueba el programa o se pueden copear y pegar a la carpeta los archivos con los cuales desea probar el mismo
# El programa reproduce cada archivo individualmente y hace correctamente dos funciones , la de transposicion y la de suma continua


#importamos las librerias y clases necesarias

from Tkinter import *
from Reproducir import Reproducir
import pyaudio
import sys
import getopt
import struct
import wave
import numpy as np








def main():

        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        status = False
        print status
        root = Tk()
        root.title("Reproduciones")

      ## Campo de texto y boton reproduccion 1
        label = Label(root, fg="black")
        label.pack()
        label.grid(row=1,column=2)
        label.config(text="Nombre o ruta (Archivo 1)")
        Nombre1 = "texto"
        Archivo = Reproducir(Nombre1)

        e1 = Entry(root)
        e1.grid(row=2,column=2,)


## llamamos las funciones respetivas de la clase Reproducir para que el audio 1 suene
        def init_audio():
            Archivo.ruta = e1.get()
            Argumentos = Archivo.abrir()
            Archivo.inicio(Argumentos[0],Argumentos[1],Argumentos[2])
            Archivo.rep()

        rep1=Button(root,text='Reproducir audio 1', command=init_audio)
        rep1.grid(row=3,column=3)




## Campo de texto y boton de reproducir 2
        label2 = Label(root, fg="black")
        label2.pack()
        label2.grid(row=4,column=2)
        label2.config(text="Nombre o ruta (Archivo 2 ) ")
        Nombre2 = "texto"
        Archivo2 = Reproducir(Nombre2)

        e2 = Entry(root)
        e2.grid(row=5,column=2)

 ## llamamos las funciones respetivas de la clase Reproducir para que el audio 2 suene
        def init_audio2():
            Archivo2.ruta = e2.get()
            Argumentos = Archivo2.abrir()
            Archivo2.inicio(Argumentos[0],Argumentos[1],Argumentos[2])
            Archivo2.rep()

        rep2=Button(root,text='Reproducir audio 2', command=init_audio2)
        rep2.grid(row=6,column=3)

## Campo de texto y boton reproduccion 3
        label3 = Label(root, fg="black")
        label3.pack()
        label3.grid(row=7,column=2)
        label3.config(text="Nombre o ruta (Archivo 3)")
        Nombre3 = "texto"
        Archivo3 = Reproducir(Nombre3)

        e3 = Entry(root)
        e3.grid(row=8,column=2,)



## llamamos las funciones respetivas de la clase Reproducir para que el audio 3 suene
        def init_audio3():
            Archivo3.ruta = e3.get()
            Argumentos = Archivo3.abrir()
            Archivo3.inicio(Argumentos[0],Argumentos[1],Argumentos[2])
            Archivo3.rep()

        rep3=Button(root,text='Reproducir audio 3', command=init_audio3)
        rep3.grid(row=12,column=3)


        def sumar(f, A, p):

            outfile = "sumaa.wav"

            wav_file = wave.open(outfile, "wb")
            nchannels = f.getnchannels()
            sampwidth = f.getsampwidth()
            framerate = f.getframerate()
            nframes = f.getnframes()
            comptype = f.getcomptype()
            compname = f.getcompname()

            wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
            tamanof =  f.getnframes()
            tamanoA =  A.getnframes()
            tamanop =  p.getnframes()
            array1 = []
            array2 = []
            array3 = []

            for i in range(0, tamanoA):
                datos1 =  struct.unpack("<h", A.readframes(1))
                array1.append(int(datos1[0]))
            for i in range(0, tamanof):
                datos2 =  struct.unpack("<h", f.readframes(1))
                array2.append(int(datos2[0]))
            for i in range(0, tamanop):
                datos3 =  struct.unpack("<h", p.readframes(1))
                array3.append(int(datos3[0]))
            wavearray=[]
            if (tamanoA >= tamanof) and tamanoA>tamanop:
                for i in range(0, tamanoA):
                    wavearray.append(array1[i])
                for i in range(0,tamanof):
                    wavearray[i]=wavearray[i]+array2[i]
                for i in range(0,tamanop):
                    wavearray[i]=wavearray[i]+array3[i]


            if (tamanof >= tamanoA)and tamanof>tamanop:
                for i in range(0, tamanof):
                    wavearray.append(array2[i])
                for i in range(0,tamanoA):
                    wavearray[i]=wavearray[i]+array1[i]
                for i in range(0,tamanop):
                    wavearray[i]=wavearray[i]+array3[i]

            if (tamanop >= tamanoA) and (tamanop > tamanof):
                for i in range(0, tamanop):
                    wavearray.append(array3[i])
                for i in range(0,tamanof):
                    wavearray[i]=wavearray[i]+array2[i]
                for i in range(0,tamanoA):
                    wavearray[i]=wavearray[i]+array1[i]

            for i in range(0,len(wavearray)):
                if wavearray[i]>32767:
                    wavearray[i]=32767
                elif wavearray[i]<-32767:
                    wavearray[i]=-32767
                wav_file.writeframes(struct.pack("<h",wavearray[i]))
            wav_file.close()




# Funcion de transpocion donde obtenemos los datos de los tres archivos llamamos la funcion sumar
# y reproduce los tres audios al tiempo


        def trs():

            card = 'default'

            opts, args = getopt.getopt(sys.argv[1:], 'c:')
            for o, a in opts:
                if o == '-c':
                    card = a
            n1=e1.get()
            n2=e2.get()
            n3=e3.get()
            f = wave.open(n1, 'rb')
            A = wave.open(n2, 'rb')
            p = wave.open(n3, 'rb')
            sumar(f, A, p)
            f.close()
            A.close()


            p.close()


            Archivo5 = Reproducir('sumaa.wav')
            Archivo5.ruta = "sumaa.wav"
            Argumentos = Archivo5.abrir()
            Archivo5.inicio(Argumentos[0],Argumentos[1],Argumentos[2])


            Archivo5.rep()

        tr=Button(root,text='Transposicion',command=trs)
        tr.grid(row=18,column=1)

# funcion de suma continua la cual toma los datos de los archivos cargados y reproduce cada audio
# uno detras del otro
        def suma():
            n1=e1.get()
            n2=e2.get()
            n3=e3.get()
            infiles = [n1, n2, n3]
            outfile = "sumaa.wav"

            data= []
            for infile in infiles:
                w = wave.open(infile, 'rb')
                data.append( [w.getparams(), w.readframes(w.getnframes())] )
                w.close()

            output = wave.open(outfile, 'wb')
            output.setparams(data[0][0])
            output.writeframes(data[0][1])
            output.writeframes(data[1][1])
            output.writeframes(data[2][1])
            output.close()


            Archivo5 = Reproducir(outfile)
            Archivo5.ruta = "sumaa.wav"
            Argumentos = Archivo5.abrir()
            Archivo5.inicio(Argumentos[0],Argumentos[1],Argumentos[2])


            Archivo5.rep()



        s=Button(root,text='Suma continua',command=suma)
        s.grid(row=18,column=2)



        def sumar2():
            n1=e1.get()
            n2=e2.get()
            n3=e3.get()
            f = wave.open(n1, 'rb')
            A = wave.open(n2, 'rb')
            p = wave.open(n3, 'rb')


            outfile = "sumaa.wav"
            wav_file = wave.open(outfile, "wb")
            nchannels = f.getnchannels()
            sampwidth = f.getsampwidth()
            framerate = f.getframerate()
            nframes = f.getnframes()
            comptype = f.getcomptype()
            compname = f.getcompname()

            wav_file.setparams((2, 2, framerate, nframes, comptype, compname))
            left=[]
            right=[]


            tamanof =  f.getnframes()
            tamanoA =  A.getnframes()
            tamanop =  p.getnframes()
            tamanoof=len(tamanof)
            tamanooA=len(tamanoA)
            tamanoop=len(tamanop)
            array1 = []



            for i in range(0, tamanoA):
                datos1 =  struct.unpack("<h", A.readframes(1))
                array1.append(int(datos1[0]))
            for i in range(0, tamanof):
                datos2 =  struct.unpack("<h", f.readframes(1))
                array1.append(int(datos2[0]))
            for i in range(0, tamanop):
                datos3 =  struct.unpack("<h", p.readframes(1))
                array1.append(int(datos3[0]))


            if (tamanooA >= tamanoof) and tamanooA>tamanoop:
                for i in range(0, tamanooA):
                    left.append(tamanoA[i][0])
                    right.append(0)
                for i in range(0,tamanoof):
                    left[i]=left[i]+tamanof[i][0]
                    right[i]=right[i]+tamanof[i][0]
                for i in range(0,tamanop):
                    right[i]=right[i]+tamanop[i][0]


            if (tamanoof >= tamanooA)and tamanoof>tamanoop:
                for i in range(0, tamanoof):
                    right.append(tamanof[i][0])
                    left.append(0)
                for i in range(0,tamanooA):
                    left[i]=left[i]+tamanoA[i][0]
                    right[i]=right[i]+tamanoA[i][0]
                for i in range(0,tamanoop):
                    left[i]=left[i]+tamanop[i][0]


            if (tamanoop >= tamanooA) and (tamanoop > tamanoof):
                for i in range(0, tamanoop):
                    left.append(tamanop[i][0])
                    right.append(tamanop[i][0])

                for i in range(0,tamanoof):
                    right[i]=right[i]+tamanof[i][0]
                for i in range(0,tamanooA):
                    left[i]=left[i]+tamanoA[i][0]


            for i in range(0,len(right)):
                if right[i]>32767:
                    right[i]=32767
                if right[i]<-32767:
                    right[i]=-32767
                if left[i]>32767:
                    left[i]=32767
                if left[i]<-32767:
                    left[i]=-32767

            print left
            print right




            stereo=""
            for i in range (0,len(right)):
                stereo+=struct.pack('h',left[i])
                stereo+=struct.pack('h',right[i])

            wav_file.writeframes(stereo)
            wav_file.close()


            Archivo6 = Reproducir('sumaa.wav')
            Archivo6.ruta = "sumaa.wav"
            Argumentos = Archivo6.abrir()
            Archivo6.inicio(Argumentos[0],Argumentos[1],Argumentos[2])


            Archivo6.rep()


        lr=Button(root,text='Suma Estereo',command=sumar2)
        lr.grid(row=18,column=3)

        salir=Button(root,text='Salir', command = root.destroy)
        salir.grid(row=23,column=3)


        a = BooleanVar(root)
        a.set(False)

        root.mainloop()



if __name__ == '__main__':
    main()
