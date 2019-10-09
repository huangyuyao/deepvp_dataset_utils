#!/bin/sh

PREFIX_URL=http://ilab.usc.edu/kai/deepvp/
for t in AL2MI.tgz australia.tgz boston.tgz BZ2CL.tgz CZ2ET.tgz indonesia.tgz japan.tgz LA2NY.tgz la_city.tgz \
la_mountain.tgz lasvegas.tgz london_city.tgz mexico.tgz MT2NC.tgz newzealand.tgz norway.tgz paris.tgz PT2IT.tgz \
russia.tgz SouthAfrica.tgz stockholm.tgz tailand.tgz TX2ND.tgz WA2FL.tgz; do
  printf "downloading $PREFIX_URL$t ..."
	if aria2c $PREFIX_URL$t >> log_deepvp_dataset.log; then
    printf "done\n"
  else
    printf "failed\n"
  fi
done
