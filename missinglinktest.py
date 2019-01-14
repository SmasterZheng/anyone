import missinglink
import tensorflow as tf

sess=tf.Session()

missinglink_project = TensorFlowProject()

with missinglink_project.create_experiment(
    display_name='MNIST multilayer perception',
    description='Two fully connected hidden layers',
    monitored_metrics={'loss': loss, 'acc': eval_correct}) as experiment:
# replace
# for step in range(MAX_STEPS):
# with 
    for step in experiment.loop(max_iterations=MAX_STEPS):
        with experiment.train():
            _, loss_value = session.run([train_op, loss], feed_dict=feed_dict)
            if (step + 1) % 500 == 0 or (step + 1) == MAX_STEPS:
                with experiment.validation():
                do_eval(session, eval_correct, images_placeholder,
                    labels_placeholder, data_sets.validation)
                    total_test_iterations = data_set.num_examples

                with experiment.test (
                    total_test_iterations,
                    expected=labels_placeholder,
                    predicted=logits 
                    ):
                    sess.run([train_op, loss], feed_dict=feed_dict)
