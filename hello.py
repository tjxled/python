#!/usr/bin/env python
i=0
j=0
k=0
while 1:
	i=i+1
	k=k+1
	j=0
	while k<100:
		j=j+1
		if j == 10000000:
			break
	if i == 10000000:
		print '10 million times'
		break
