"""Creates a TF model to classify png images based on damage.

Functions as main for training. Stores the model for future testing.
"""

import classifier_constants as cc
import image_handler as im_h
import tensorflow as tf
import numpy as np

import time

# Load data.
data = im_h.Data(cc.PATH_TO_CSV_MAP)

print "Data Loaded"
# Graph input.
images = tf.placeholder('float', [None, cc.NUM_INPUT_NEURONS])
labels = tf.placeholder('float', [None, cc.NUM_OUTPUT_NEURONS])

def multilayer_perceptron(images, weights, biases):
    """Creates the TF model.

    Args:
        images: [image num, image_size] of png pixel data
        weights: {} with w1, w2, wout, rep weights between layers
        biases: {} with b1, b2, bout, rep biases between layers
    """
    # Each hidden layer is a relu activation neuron with wx + b synapse.
    layer_1 = tf.add(tf.matmul(images, weights['w1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)

    layer_2 = tf.add(tf.matmul(layer_1, weights['w2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)

    # Output layer is linear.
    out = tf.matmul(layer_2, weights['wout']) + biases['bout']
    return out

def main():
    # Store layers weight & bias.
    weights = {
        'w1': tf.Variable(tf.random_normal([cc.NUM_INPUT_NEURONS,
                                            cc.N_HIDDEN_1])),
        'w2': tf.Variable(tf.random_normal([cc.N_HIDDEN_1, cc.N_HIDDEN_2])),
        'wout': tf.Variable(tf.random_normal([cc.N_HIDDEN_2,
                                              cc.NUM_OUTPUT_NEURONS]))
    }
    biases = {
        'b1': tf.Variable(tf.random_normal([cc.N_HIDDEN_1])),
        'b2': tf.Variable(tf.random_normal([cc.N_HIDDEN_2])),
        'bout': tf.Variable(tf.random_normal([cc.NUM_OUTPUT_NEURONS]))
    }

    saver = tf.train.Saver(dict(weights.items() + biases.items()))

    model = multilayer_perceptron(images, weights, biases)
    # Use adam optimizer because >>> than gradient descent, converges faster.
    cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(model, labels))
    opt = tf.train.AdamOptimizer(learning_rate=cc.LEARNING_RATE).minimize(cost)

    print "Starting sess"

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())

        #reload old model if it previously exists
        ckpt = tf.train.get_checkpoint_state(cc.PATH_TO_MODEL)
        if ckpt and ckpt.model_checkpoint_path:
            print "Loaded old model"
            saver.restore(sess, ckpt.model_checkpoint_path)

        for epoch in range(cc.TRAINING_EPOCHS):
            avg_cost = 0
            total_batch = int(cc.NUM_EXAMPLES/cc.BATCH_SIZE)

            start = time.clock()
            for _ in xrange(total_batch):
                data_df = data.get_next_batch(cc.BATCH_SIZE)

                batch_images = data_df['data'].tolist()
                batch_labels = data_df['label'].tolist()

                _, c = sess.run([opt, cost], feed_dict={images: batch_images,
                                                        labels: batch_labels})
                avg_cost += c/total_batch

            print time.clock() - start

            if epoch % cc.DISPLAY_STEP == 0:
                print('Epoch:', '%04d' % (epoch+1), 'cost=', \
                      '{:.9f}'.format(avg_cost))

        saver.save(sess, cc.PATH_TO_MODEL + cc.MODEL_NAME)

        # Testing. Currently tests on self, but damage classifier should ideally
        # have 100% accuracy because important neurons shouldn't change.
        correct_prediction = tf.equal(tf.argmax(model, 1), tf.argmax(labels, 1))
        predictions = tf.argmax(model, 1)
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        data_df = data.get_next_batch(cc.BATCH_SIZE)
        batch_images = data_df['data'].tolist()
        batch_labels = data_df['label'].tolist()
        start = time.clock()
        print predictions.eval(feed_dict={images: batch_images,
                                          labels: batch_labels})
        print [np.argmax(x) for x in batch_labels]
        print time.clock() - start
        print("Accuracy:", accuracy.eval({images: batch_images,
                                          labels: batch_labels}))

main()
