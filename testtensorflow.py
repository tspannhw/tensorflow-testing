import tensorflow as tf
 
tf.__version__sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

print(tf.__version__sess)
