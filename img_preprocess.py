import cv2 #opencv 사용
import time

def main(): 
    camera = cv2.VideoCapture(-1) # -1 기본값
    camera.set(3, 640)
    camera.set(4, 480)
    #filepath = "/home/pi/AI_CAR/video/test" # 파일의 경로와 저장될 이름을 대입한다.
    #i = 0 # 사진 번호를 붙일 숫자값 변수를 만들고 0으로 초기화한다.

    while (camera.isOpened()): # 카메라 동작하면 (+ 키값 읽어 출력하는 부분)
        #keyValue = cv2.waitKey(10) # 키보드 값을 입력받는다, 0.001초 동안 읽히지 않으면 timeout 발생
    
        #if keyValue == ord('q'): # q값을 입력받으면 break
        #    break
       
        #img_preprocessing    
        _, image = camera.read() # 프레임 값을 읽어 image변수에 저장
        image = cv2.flip(image, -1) # -1은 180도 이미지를 뒤집는다
        cv2.imshow ('Original', image) # 원본 출력
        
        preprocessed = img_preprocess(image)
        cv2.imshow('preprocess', preprocessed) # 전처리 출력

def img_preprocess(image):
    height, _, _ = image.shape # 높이를 변수에 저장한다
    image = image[int(height/2):,:,:] # 높이를 이용해 가로로 1/2 중간지점을 자르고 -> 윗부분 날리고 아랫부분 남김
    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV) # 색변환 -> 인공지능학습을 위한 전처리, 효율적으로 특징을 잡아내 인식율 up
    image = cv2.resize(image, (200,66)) # 사이즈변환 -> 속도 up
    image = cv2.GaussianBlur(image,(5,5),0) # 블러처리 -> 픽셀간의 차이를 낮춘다 -> 영상에 존재하는 잡음의 영향을 제거해 인식률 up
    _,image = cv2.threshold(image,160,255,cv2.THRESH_BINARY_INV) # 임계점 이상의 값을 최대값으로 바꾸어 라인 인식율을 증가시킴
    # 입계점 설정에 따라서 선을 인식하는 범위가 틀려진다. 빛과 라인 색상에 따라 틀리다 -> 상황에 맞게 설정하기
    return image

        #cv2. imwrite("%S_%05d.png" % (filepath, i), image) # 이미지를 저장하는 함수
        #i = i + 1

        #time.sleep(1.0) # 1초마다 사진이 갱신된다
    
    # cv2.destroyAllWindows() # 모든 opencv 창 종료
