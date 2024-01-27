start_date = input()
s_li = start_date.split(" ")
start = int(s_li[1])

h_m_s = input()
h_m_s_li = h_m_s.split(":")
hour = int(h_m_s_li[0])
minute = int(h_m_s_li[1])
second = int(h_m_s_li[2])

end_date = input()
s_li2 = end_date.split(" ")
end = int(s_li2[1])

h_m_s1 = input()
h_m_s_li1 = h_m_s1.split(":")
hour1 = int(h_m_s_li1[0])
minute1 = int(h_m_s_li1[1])
second1 = int(h_m_s_li1[2])

total_sec = ((end-start)*24*3600) + ((hour1-hour)*3600) + ((minute1- minute)*60) + (second1-second)

day = total_sec//(24*3600)
remain_sec = total_sec%(24*3600)
hour = remain_sec // 3600
remain_sec = remain_sec%3600
minute = remain_sec//60
second = remain_sec % 60

print("%d dia(s)" %day)
print("%d hora(s)" %hour)
print("%d minuto(s)" %minute)
print("%d segundo(s)" %second)
