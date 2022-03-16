#!/usr/bin/env bash
# cerner_2tothe5th_2021

# yeah i know, it gets created in /tmp but who knows where this is being ran
cow=$(mktemp)

# bash is cheating
if [[ $1 ]]; then input=${1}; else echo "What does the cow say?":; read -r input; fi

# dynamically create the box
dash="";i=0; while [[ ${#input}+4 -gt ${i} ]]; do ((i+=1));dash+="-"; done

# populate tmp file
echo -e "${dash}" >> ${cow}; echo -e "< ${input} >" >> ${cow}; echo -e "${dash}" >> ${cow}
echo -n "
        \   ^__^
         \  (oo)\_______
            (__)\       )\//\\
                ||----w |
                ||     ||
" >>${cow}

# doesn't need to be awk, but why not
awk -v seed=$RANDOM  'BEGIN {srand(seed);} {printf("\033[38;5;%dm%s\033[0m",r[i]=int(rand()*255+1), $0);} {printf("\n");}' ${cow}

# cleanup
rm -f ${cow} 1>/dev/null 2>&1
