#!/usr/bin/env python
# coding: utf-8

import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor


preprocessor = create_preprocessor('xception', target_size=(224, 224))


interpreter = tflite.Interpreter(model_path='clothing-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


classes=['AppleApplescab',
 'AppleBlackrot',
 'AppleCedarapplerust',
 'Applehealthy',
 'Blueberryhealthy',
 'Cherry(includingsour)Powderymildew',
 'Cherry(includingsour)healthy',
 'Corn(maize)Cercosporaleafspot Grayleafspot',
 'Corn(maize)Commonrust',
 'Corn(maize)NorthernLeafBlight',
 'Corn(maize)healthy',
 'GrapeBlackrot',
 'GrapeEsca(BlackMeasles)',
 'GrapeLeafblight(IsariopsisLeafSpot)',
 'Grapehealthy',
 'OrangeHaunglongbing(Citrusgreening)',
 'PeachBacterialspot',
 'Peachhealthy',
 'Pepper,bellBacterialspot',
 'Pepper,bellhealthy',
 'PotatoEarlyblight',
 'PotatoLateblight',
 'Potatohealthy',
 'Raspberryhealthy',
 'Soybeanhealthy',
 'SquashPowderymildew',
 'StrawberryLeafscorch',
 'Strawberryhealthy',
 'TomatoBacterialspot',
 'TomatoEarlyblight',
 'TomatoLateblight',
 'TomatoLeafMold',
 'TomatoSeptorialeafspot',
 'TomatoSpidermites Two-spottedspidermite',
 'TomatoTargetSpot',
 'TomatoTomatoYellowLeafCurlVirus',
 'TomatoTomatomosaicvirus',
 'Tomatohealthy']


# url = 'https://raw.githubusercontent.com/AsMoh/Plant-Diseases-Classification/main/Cornheal.jpg'


def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()
    indx=np.argmax(float_predictions)
    
    return classes[indx])


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result


