while true; do
python3 screen.py
mDate="$(date +%Y-%m-%d)"
mTime="$(date +%H-%M-%S)"
echo $mTime
mkdir ./$mDate
mv ./screen.png ./$mDate/$mTime.png
sleep 5
done