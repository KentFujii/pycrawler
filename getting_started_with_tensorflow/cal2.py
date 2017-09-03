import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

cal1_op = a + b * c
cal2_op = (a + b) * c

sess = tf.Session()
res1 = sess.run(cal1_op)
print(res1)
res2 = sess.run(cal2_op)
print(res2)
