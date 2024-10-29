#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

input_str = """1 345255357 205970905
1 570256166 75865401
1 94777800 645102173
1 227496730 16649450
1 82987157 486734305
1 917920354 757848208
1 61379773 817694251
1 330547128 112869154
1 328743001 855677723
1 407951306 669798718
1 21506172 676980108
1 49911390 342109400
1 980306253 305632965
2 736380701 402184046
2 798108301 416334323
1 254839279 1370035
1 109701362 2800586
1 374257441 165208824
1 624259835 477431250
1 629066664 454406245
1 135821145 763845832
1 480298791 138234911
1 553575409 835718837
1 13022848 624652920
1 974893519 882630870
1 137832930 216177975
1 453349691 969255659
1 138396076 91038209
1 699822497 941751038
1 116800806 64071662
1 815273934 8835809
1 658534867 657771609
1 183760807 179377441
1 93984556 636425656
1 231506463 836238924
1 214074594 709571211
1 649641434 509698468
2 523656673 709717705
2 261443586 330808140
1 75924023 449768243
1 849537714 354568873
2 641743742 124196560
1 19829224 995759639
1 244389335 108315212
1 877758467 421383626
1 573278148 474192994
2 561031511 448889978
1 773294404 980994962
2 33088709 716646168
1 760927835 441983538
1 273540687 783321829
1 5933845 384358662
1 543628702 372160176
2 136400466 910559291
2 546568738 393221347
1 812227065 694221123
1 311065574 103905420
2 571344361 185289590
1 99638520 173318136
1 854060080 407068012
2 980658213 778573744
2 412539660 476853104
1 530145366 36493537
1 604875364 100141497
2 650812104 64817757
1 141060009 766603553
1 598398952 418245941
1 262344011 431865586
2 56413893 546484833
1 400736735 673588153
1 642955232 803851098
1 917782037 935143105
1 658284524 745224102
1 103202288 501551287
1 162144918 12888783
1 16486753 67467208
1 671120703 941541277
1 47399694 77707668
1 122011395 946116527
1 924363862 886726236
2 657761235 540240467
1 203175991 279882007
2 304620923 162838413
1 440453449 117964712
2 941868853 887850334
1 293198923 466812643
1 461688477 532794906
1 315016797 733095902
1 265008751 913972757
1 887405255 139170948
2 754223230 426836947
1 945967814 852589735
1 168866283 309720694
1 373861145 94596540
2 984122495 20702849
2 233835636 180460242
1 172787631 643823473
1 273611372 616819555
1 196104599 690080895
1 527554061 434103342"""


def dynamicArray(n, Q):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    ans = []
    for q in Q:
        idx = (q[1] ^ lastAnswer) % n
        if q[0] == 1: 
            arr[idx].append(q[2])
        elif q[0] == 2:
            z = q[2] % len(arr[idx])
            lastAnswer = arr[idx][z]
            ans.append(lastAnswer)
            print(lastAnswer)
    return


if __name__ == '__main__':
    n = 100; q = 100
    queries = []

    for each in input_str.split('\n'):
        queries.append(list(map(int, each.split())))

    dynamicArray(n, queries)

