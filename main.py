# Импорт всех библиотек 
import cv2

# Установка значений для основных переменных
img = cv2.imread("images/1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Подключение модели
faces = cv2.CascadeClassifier('faces.xml')

# Сканирование фото и определение размера
results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# Вырисовка контуров
for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

# Показ результата
cv2.imshow("Result", img)
cv2.waitKey(0)
