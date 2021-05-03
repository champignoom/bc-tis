scale = 10
for (i=0; i<10; i++) {
  for (j=1; j<10; j++) b=i*j
}
b
for (i=0; i<10; i++) {
  for (j=10000000000000; \
       j<10000000000010; \
       j++) b=i*j
}
b
quit

