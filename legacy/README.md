
    # guess transations in prepost.py

    # add csv data into data/new_raws/
    bash slurp_raw.sh
    cat accounts.beancount beans_my/* > /tmp/my.beancount; bean-check /tmp/my.beancount
    
    echo To run fava:
	echo fava /tmp/my.beancount
