# move_forward(xp, yp, xg, yg, direction, obstacles, m, n):
#     if direction = "right" and xp + 1 > n and [xp + 1, yp] not in obstacles and [xp + 1, yp] != [xg, yg]:
#         xp += 1
#         return xp + 1, yp
#     if direction = "left" and xp - 1 > 0 and[xp - 1, yp] not in obstacles and[xp - 1, yp] !=[xg, yg]:
#         xp -= 1
#         return xp - 1, yp
#     if direction = "up" and yp + 1 < m and[xp, yp + 1] not in obstacles and[xp, yp + 1] !=[xg, yg]:
#         yp += 1
#         return xp, yp + 1
#     if direction = "down" and yp - 1 > 0 and[xp, yp - 1] not in obstacles and[xp, yp - 1] !=[xg, yg]:
#         yp -= 1
#         return xp, yp - 1