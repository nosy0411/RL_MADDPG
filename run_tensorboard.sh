# !/bin/bash
tensorboard --logdir=./log/ --port=3000 &> /dev/null &
echo "Wait around 10 seconds and open this link at your browser (ignore other outputs):"
echo "https://$WORKSPACEID-3000.$WORKSPACEDOMAIN"