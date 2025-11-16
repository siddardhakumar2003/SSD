# Write YOUR code here
declare -i lines=$1
if [[ $lines -le 0 ]]; then
    echo "Invalid input"
    exit 0
fi
declare line=1 
while [[ $line -le $lines ]]; do
    declare j=1
    while [[ $j -le $((lines - line)) ]]; do
        echo -n "  "
        ((j++))
    done
    declare i=1
    while [[ $i -le $((2*line -1)) ]]; do
        echo -n $i" "
        ((i++))
    done
    echo ""
    ((line++))
done

