import math
total=23
Grade={'O':10,'A+':9,'A':8,'B+':7,'B':6,'RA':0}
subjects=["Technical English:","Complex Functions and Laplace Transforms:","Physics for Information Science:","Environmental Science:","Basic Electrical, Electronics and Measurement Engineering:","Programming in C:","Design Thinking and Engineering Practices Lab:","Programming in C Lab:"]
credits=[3,4,3,3,3.5,3.5,1.5,1.5]
sum=0
print("ENTER GRADE FOR FOLLOWING SUBJECTS:")
for i in range(0,8,1):
    g=input(subjects[i])
    sum+=credits[i]*Grade[g]
print("Your Grade is",'%.2f'%(sum/total))
