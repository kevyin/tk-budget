
bean-report -f text /tmp/my.beancount balances | grep -e Assets:Westpac
if [ $1 == "equity" ]; then
    bean-report -f text /tmp/my.beancount balances | grep -e Assets:Westpac | tr -s ' ' '\t' | awk '{sum+=$2} END {print sum}'

elif [ $1 == "networth" ]; then
    bean-report -f text /tmp/my.beancount balances | grep -e Assets:Westpac -e Assets:Property -e Liabilities | tr -s ' ' '\t' | awk '{sum+=$2} END {print sum}'
else
	echo "finances.sh [networth|equity]"
fi
