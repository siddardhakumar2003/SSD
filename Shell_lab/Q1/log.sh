# Write YOUR code here
declare -a aditya=(0 0)
declare -a rohan=(0 0)
declare -a sneha=(0 0)

for file in logs/*.log; do
    while read -r line; do
        IFS=" " read -a words <<< $line
        if [[ "${words[4]}" == "failed" && "${words[5]}" == "login" ]]; then 
            case "${words[3]}" in 
            "Aaditya")  ((aditya[1]++));;
            "Rohan")  ((rohan[1]++));;
            "Sneha")  ((sneha[1]++));;
            esac
        else 
            if [[ "${words[4]}" == "logged" && "${words[5]}" == "in" ]]; then
                case "${words[3]}" in 
                "Aaditya") ((aditya[0]++));;
                "Rohan") ((rohan[0]++));;
                "Sneha") ((sneha[0]++));;
                esac
            fi
        fi
    done < "$file"
done  

echo "Aaditya   : ${aditya[0]} success, ${aditya[1]} fail"
echo "Rohan     : ${rohan[0]} success, ${rohan[1]} fail"
echo "Sneha     : ${sneha[0]} success, ${sneha[1]} fail"