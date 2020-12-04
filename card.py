#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


# Colors
RED = 'r'
BLUE = 'b'
GREEN = 'g'
YELLOW = 'y'
BLACK = 'x'

COLORS = (RED, BLUE, GREEN, YELLOW)

COLOR_ICONS = {
    RED: '❤️',
    BLUE: '💙',
    GREEN: '💚',
    YELLOW: '💛',
    BLACK: '⬛️'
}

# Values
ZERO = '0'
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
DRAW_TWO = 'draw'
REVERSE = 'reverse'
SKIP = 'skip'

VALUES = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, DRAW_TWO,
          REVERSE, SKIP)
WILD_VALUES = (ONE, TWO, THREE, FOUR, FIVE, DRAW_TWO, REVERSE, SKIP)

# Special cards
CHOOSE = 'colorchooser'
DRAW_FOUR = 'draw_four'

SPECIALS = (CHOOSE, DRAW_FOUR)

STICKERS = {
    'b_0': 'CAACAgEAAxkBAALc0l_DwUVQz2W9oiQXIWgqtfNeO6VTAAL0BwACCH26AqDCFn2P38gpHgQ',
    'b_1': 'CAACAgEAAxkBAALc1F_DwUfQxCRRFUcBkvzvUs7_P6GNAAL1BwACCH26AtY2X-dj32wsHgQ',
    'b_2': 'CAACAgEAAxkBAALc1l_DwUhUli4emqSeFWv-ITVed_JsAAL2BwACCH26AndXAcfi8OrlHgQ',
    'b_3': 'CAACAgEAAxkBAALc2F_DwUk9LEyoLkwAAVCqp-WZjZaiyAAC9wcAAgh9ugKrH28EuWejnR4E',
    'b_4': 'CAACAgEAAxkBAALc2l_DwUpVw-XH_JUOiL37ZAcIqRWCAAL4BwACCH26ArWUZWCrKICsHgQ',
    'b_5': 'CAACAgEAAxkBAALc3F_DwUsm_L3aTGYXYfci6bqLkWhaAAL5BwACCH26AsfIlas3cE8EHgQ',
    'b_6': 'CAACAgEAAxkBAALc3l_DwUzSI_xYeMX69zPrXcg_DM_LAAL6BwACCH26Ar85R8gU7dndHgQ',
    'b_7': 'CAACAgEAAxkBAALc4F_DwU0KvxCgXvUu-XPa3lP0wjMiAAL7BwACCH26AiDMQAlLep78HgQ',
    'b_8': 'CAACAgEAAxkBAALc4l_DwU6bKEwewz0TGIhUYchyWn3GAAL8BwACCH26AiLKSuVLQXH5HgQ',
    'b_9': 'CAACAgEAAxkBAALc5F_DwU9gFoBoICz1W4N_Nf9zP-pDAAL9BwACCH26Aku1dt_3cEXrHgQ',
    'b_draw': 'CAACAgEAAxkBAALc5l_DwVBfOV3dD3BlGWCwthsAAYiasAAC_gcAAgh9ugJfdR2xh6gs1B4E',
    'b_reverse': 'CAACAgEAAxkBAALc6F_DwVGya19O5jYVIVWa7yrCQa_2AAL_BwACCH26AuUcXE9EAAEqTR4E',
    'b_skip': 'CAACAgEAAxkBAALc6l_DwVLvOoVf4k2nZ4jPS-LkEX5NAAMIAAIIfboCMD-BRtXFy18eBA',
    'g_0': 'CAACAgEAAxkBAALc7F_DwVNqkvpaOnpB5nsTiEKz6yu4AAIBCAACCH26Am17v6rt36YsHgQ',
    'g_1': 'CAACAgEAAxkBAALc7l_DwVQcxb6X2sh0JTX-De63u7AHAAICCAACCH26Arn0qDHcZ7PFHgQ',
    'g_2': 'CAACAgEAAxkBAALc8F_DwVbUUSBVRqKKZkNX1ZvUuX9sAAIDCAACCH26AnTaVjfJvlivHgQ',
    'g_3': 'CAACAgEAAxkBAALc8l_DwVdEt0XXiEF-UMV7rZLiuW2DAAIECAACCH26AmC89Q5JsIhAHgQ',
    'g_4': 'CAACAgEAAxkBAALc9F_DwVg37xHywkl_698XMnzRVEnhAAIFCAACCH26AogMCBPl2fJBHgQ',
    'g_5': 'CAACAgEAAxkBAALc9l_DwVmuw4BtEPJNA9SVNX_aCYV5AAIGCAACCH26AtZvmPaMKJ70HgQ',
    'g_6': 'CAACAgEAAxkBAALc-F_DwVqCSpWX0Lg-I2KrDPorSj-cAAIHCAACCH26AuIhZjMTmK62HgQ',
    'g_7': 'CAACAgEAAxkBAALc-l_DwVvKBb5Q0tkQpXR36b8MZBjrAAIICAACCH26ApHlJLhXiYkbHgQ',
    'g_8': 'CAACAgEAAxkBAALc_F_DwVymVWQOMUmpa3Oc3jRU6atlAAIJCAACCH26AlUV_wovbqtBHgQ',
    'g_9': 'CAACAgEAAxkBAALc_l_DwV03UX585aQEPFTLt0fMLRt2AAIKCAACCH26AjCP8otr_0OcHgQ',
    'g_draw': 'CAACAgEAAxkBAALdAAFfw8FeB7WNV3JPZca40zcDlk49owACCwgAAgh9ugKaPC7Yzf8aFR4E',
    'g_reverse': 'CAACAgEAAxkBAALdAl_DwV9Ok0HFe-O8G76dDsuWjRuMAAIMCAACCH26AiHjoq64JjL8HgQ',
    'g_skip': 'CAACAgEAAxkBAALdBF_DwWAcXm2TLhIGqQ78AdYcqrzMAAINCAACCH26Anh32o0-AkOTHgQ',
    'r_0': 'CAACAgEAAxkBAALdBl_DwWGqDdoOVEZ0J6fdF8D1XKpSAAIOCAACCH26AtfVjktfQRVGHgQ',
    'r_1': 'CAACAgEAAxkBAALdCF_DwWJil5MW0bPUkV8LchsQ56u7AAIPCAACCH26Al_R9eavwWuRHgQ',
    'r_2': 'CAACAgEAAxkBAALdCl_DwWN-y9ITDDu0Gp4qsXF4bfyZAAIQCAACCH26AgwsrbjGJ_WaHgQ',
    'r_3': 'CAACAgEAAxkBAALdDF_DwWTWBuRfHxSana0STjMBY-t4AAIRCAACCH26Ag7M9PHHnKzzHgQ',
    'r_4': 'CAACAgEAAxkBAALdDl_DwWUukHkBj-q7vvRpCJ7-noQLAAISCAACCH26AvA7uEa5XOG2HgQ',
    'r_5': 'CAACAgEAAxkBAALdEF_DwWYhmEboTYAJkVp5FoTtUMWCAAITCAACCH26AsANgx3yY2LpHgQ',
    'r_6': 'CAACAgEAAxkBAALdEl_DwWfRCo3ovLliDxeBkG82Q22eAAIUCAACCH26ArI7_93XysJeHgQ',
    'r_7': 'CAACAgEAAxkBAALdFF_DwWinZ7-h8fIObnPl-ijB0_WMAAIVCAACCH26AhknsRilYIRcHgQ',
    'r_8': 'CAACAgEAAxkBAALdFl_DwWnQ0oEJ74YbodTzh3re5h4UAAIWCAACCH26Annbtds_TLWwHgQ',
    'r_9': 'CAACAgEAAxkBAALdGF_DwWs1Bl5OCCHuKdh_Lj2gZI8mAAIXCAACCH26AvOAfI6W3tYOHgQ',
    'r_draw': 'CAACAgEAAxkBAALdGl_DwW01oPUzbm-9sRepfWhWb6ouAAIYCAACCH26AulCawFv66HuHgQ',
    'r_reverse': 'CAACAgEAAxkBAALdHF_DwW9KpSCS59A32QJCAAG9pnMvUAACGQgAAgh9ugILLxZjZ47Tix4E',
    'r_skip': 'CAACAgEAAxkBAALdHl_DwXDwCgNgTLU-Zso5zImaoqNPAAIaCAACCH26AoCtRWPEozRlHgQ',
    'y_0': 'CAACAgEAAxkBAALdIF_DwXJCWCDwLp1Hyn_ekw8Xl9bHAAIbCAACCH26AsOKrtuDPg8oHgQ',
    'y_1': 'CAACAgEAAxkBAALdIl_DwXXXbA3-gtXcppc_XUJeLntJAAIcCAACCH26AoqtrX5FXYeXHgQ',
    'y_2': 'CAACAgEAAxkBAALdJF_DwXZKBR_PLR9HZPz8xOnKMhVkAAIdCAACCH26AhRcZ9HcoK6xHgQ',
    'y_3': 'CAACAgEAAxkBAALdJl_DwXfIvZY6E78iH_X0P5asDAWsAAIeCAACCH26AotJyyQSMeRbHgQ',
    'y_4': 'CAACAgEAAxkBAALdKF_DwXgv35BYXMroUei8NjLngayKAAIfCAACCH26AkFlkFqeGYN1HgQ',
    'y_5': 'CAACAgEAAxkBAALdKl_DwXnW07lt8lWRVT3fnk0xYR-6AAIgCAACCH26AvcBhhHTLvKqHgQ',
    'y_6': 'CAACAgEAAxkBAALdLF_DwXrZ3Xvx9eiVMxog2K51w-e2AAIhCAACCH26AtGSTD-kK5wIHgQ',
    'y_7': 'CAACAgEAAxkBAALdLl_DwXtAWHAfi3eTMI2Dxx7Z2YvgAAIiCAACCH26Ago84JoJv34gHgQ',
    'y_8': 'CAACAgEAAxkBAALdMF_DwXwbt3pjXI36OY-ezN3Fi-W9AAIjCAACCH26Ahe7IqeylocqHgQ',
    'y_9': 'CAACAgEAAxkBAALdMl_DwX2JBtZVxksAAZHk6SZtPQHzkgACJAgAAgh9ugIjUH5TGiw0TB4E',
    'y_draw': 'CAACAgEAAxkBAALdNF_DwX4MggOzPuWT86cgU_N3gD2gAAIlCAACCH26AoW0mlRKwjIEHgQ',
    'y_reverse': 'CAACAgEAAxkBAALdNl_DwX8gAlP_n_6TlBNDzxNOR5drAAImCAACCH26AmRn3MvRcfTkHgQ',
    'y_skip': 'CAACAgEAAxkBAALdOF_DwYEqrQLBuoXuOx45lfVz65weAAInCAACCH26ApiHdIlnX3SqHgQ',
    'colorchooser': 'CAACAgEAAxkBAALdOl_DwYJ6GYMOslVuDQ7IOBmM4ZAcAAIoCAACCH26Aq05PN0UUdTkHgQ',
    'draw_four': 'CAACAgEAAxkBAALdPF_DwYPdQH2QAZ2MnfTyf6s89pW8AAIpCAACCH26AvfUnZR-FdiwHgQ',
    'option_bluff': 'CAACAgEAAxkBAALdql_DwhcUJ5ouMRXPe__d9iUy-JOmAAJgCAACCH26Atf9tLDlZrlFHgQ',
    'option_draw': 'CAACAgEAAxkBAALdrF_Dwh0RCioKGZ-qHfXTVTo_mmWeAAJiCAACCH26AgjkSf6uJQTHHgQ',
    'option_info': 'CAACAgEAAxkBAALdrl_DwiLXz7wkXC16L9mAR88VMctNAAJjCAACCH26AsHGrj7iAoq3HgQ',
    'option_pass': 'CAACAgEAAxkBAALdsF_DwiaM7Q7HLdBgRk8lbH9YKu7lAAJlCAACCH26AhCd-9p_lgKDHgQ'
}

STICKERS_GREY = {
    'b_0': 'CAACAgEAAxkBAALdPl_DwbPzLe3A994Xioyw6C3FT3NFAAIqCAACCH26Al5UTDHn53lrHgQ',
    'b_1': 'CAACAgEAAxkBAALdQF_DwbQ21AxmNw5RA8BQrRhCLFKqAAIrCAACCH26An3RHtbVuXt5HgQ',
    'b_2': 'CAACAgEAAxkBAALdQl_DwbXXkZzCOywIhaVEYMA2vxiJAAIsCAACCH26AmL4KI87RDj6HgQ',
    'b_3': 'CAACAgEAAxkBAALdRF_DwbdmIm6sH0ya2F2MQt4E2e-WAAItCAACCH26Aj5zpAABOoqS1x4E',
    'b_4': 'CAACAgEAAxkBAALdRl_DwbhE10QR_DKsYKr_HBBkXK89AAIuCAACCH26Ao-WGyAwwtodHgQ',
    'b_5': 'CAACAgEAAxkBAALdSF_Dwbla8KG1zExRX_xzhjKDUJnmAAIvCAACCH26AmRDhGNEHFKOHgQ',
    'b_6': 'CAACAgEAAxkBAALdSl_DwboubqFcJvVb49I4rdIVZmm9AAIwCAACCH26ApR8A2MghDiGHgQ',
    'b_7': 'CAACAgEAAxkBAALdTF_DwbuFj0rWtzesU2VPOoitRzYOAAIxCAACCH26AmTew73vHxmeHgQ',
    'b_8': 'CAACAgEAAxkBAALdTl_DwbwVw2wFfevSbfCRMHdNgkwbAAIyCAACCH26AuILOG2lfD5bHgQ',
    'b_9': 'CAACAgEAAxkBAALdUF_Dwb1nLbWLHU2Lt-bkoP8h4luoAAIzCAACCH26Ar8f7veLOwfrHgQ',
    'b_draw': 'CAACAgEAAxkBAALdUl_Dwb60QMbRq4szNU1TrQOMVIEHAAI0CAACCH26AuzpKniffMKKHgQ',
    'b_reverse': 'CAACAgEAAxkBAALdVF_Dwb-BT0_00Pu4RQVWwu7x_KoPAAI1CAACCH26AjtLTBFxc3iFHgQ',
    'b_skip': 'CAACAgEAAxkBAALdVl_DwcDWR_1BB7dJ5BPihnIOEqlVAAI2CAACCH26Aoast9ZzAWlrHgQ',
    'g_0': 'CAACAgEAAxkBAALdWF_DwcEt8d-y2iha95pzZ-gB1JtpAAI3CAACCH26AjJn56O4l7sNHgQ',
    'g_1': 'CAACAgEAAxkBAALdWl_DwcJyioIAAQgUQ8l-uXvL0lP7OwACOAgAAgh9ugKSLjwkfieq5B4E',
    'g_2': 'CAACAgEAAxkBAALdXF_DwcNEJkFFpgX_8x3CAAEedex_eQACOQgAAgh9ugIjxdE-muy7vh4E',
    'g_3': 'CAACAgEAAxkBAALdXl_DwcSlupMsP27zyqWEFNgs-8V2AAI6CAACCH26ArNwRabGAeU8HgQ',
    'g_4': 'CAACAgEAAxkBAALdYF_DwcUVwbzsZ6pmoDdu6KboT3HBAAI7CAACCH26Ai7tXChW57J8HgQ',
    'g_5': 'CAACAgEAAxkBAALdYl_Dwcaq07Q_0nwS4tDScqUspl-9AAI8CAACCH26AsWCdg3RrvVWHgQ',
    'g_6': 'CAACAgEAAxkBAALdZF_DwccnkTXhG3dWsC5JcpdZX4kJAAI9CAACCH26AmfgJLc2_2pGHgQ',
    'g_7': 'CAACAgEAAxkBAALdZl_DwciXOBjD39baTZWlsQk9q9TLAAI-CAACCH26ArbDrl7vVC8JHgQ',
    'g_8': 'CAACAgEAAxkBAALdaF_DwckwDui0ubPTu-FOyskgMVqTAAI_CAACCH26AtBalH4cJp6hHgQ',
    'g_9': 'CAACAgEAAxkBAALdal_DwcpRH57deGwZUp6lB1xBYTv6AAJACAACCH26At4WDokn4byxHgQ',
    'g_draw': 'CAACAgEAAxkBAALdbF_Dwcu8NMZ08aQXyYLcdiowVuzxAAJBCAACCH26AkneEwgBxIEQHgQ',
    'g_reverse': 'CAACAgEAAxkBAALdbl_Dwcw1OVDqnfF51kxZlmIL6XwnAAJCCAACCH26Aoxn7eFankGAHgQ',
    'g_skip': 'CAACAgEAAxkBAALdcF_Dwc3LZWd_8v18YwIGjgTadLIWAAJDCAACCH26AngwqvVuM7ZUHgQ',
    'r_0': 'CAACAgEAAxkBAALdcl_Dwc7a_NuIYSq1AaFbbhIAAW2mFQACRAgAAgh9ugIwI-hCoZjOqR4E',
    'r_1': 'CAACAgEAAxkBAALddF_DwdDiXVQlWlNP2dTlIBYyv1T-AAJFCAACCH26Aq1sxvCLxcivHgQ',
    'r_2': 'CAACAgEAAxkBAALddl_DwdE1qeSApCDVKOOajNFbRaOOAAJGCAACCH26AqM4UE3AXC-FHgQ',
    'r_3': 'CAACAgEAAxkBAALdeF_DwdIj_eQSeIIKEigPYxKc1Dn9AAJHCAACCH26AuyLf6ME3rJEHgQ',
    'r_4': 'CAACAgEAAxkBAALdel_DwdOxwUFae6I9b48xhP-SuZXDAAJICAACCH26AiR66WUlYqPPHgQ',
    'r_5': 'CAACAgEAAxkBAALdfF_DwdTzwmFubxv1Zz-z4zafMXOLAAJJCAACCH26AoVTalSO3zfDHgQ',
    'r_6': 'CAACAgEAAxkBAALdfl_DwdVOxKHW1_Gzze3B3jHXqkHeAAJKCAACCH26AjH8Y5qWSqnqHgQ',
    'r_7': 'CAACAgEAAxkBAALdgF_DwdZ2B8NEYn_Q2GlJlKRMYAMuAAJLCAACCH26Ahxc95A1ouT4HgQ',
    'r_8': 'CAACAgEAAxkBAALdgl_DwddYn5ZnlDwjdoCJplpuRpEdAAJMCAACCH26AkM3A3hw2DwiHgQ',
    'r_9': 'CAACAgEAAxkBAALdhF_Dwdj4T5Argtcas2Kuq8SoM17dAAJNCAACCH26AqT1obdGT1MaHgQ',
    'r_draw': 'CAACAgEAAxkBAALdhl_DwdnoqMeABqFhC6YSwEyiDPkCAAJOCAACCH26AhC1OGuGFDxjHgQ',
    'r_reverse': 'CAACAgEAAxkBAALdiF_DwdqBaH9Av7_30g9Gbwl3eDtiAAJPCAACCH26AixkkxRCI4xzHgQ',
    'r_skip': 'CAACAgEAAxkBAALdil_DwdtoVo1Uvz7ySE5RbirTVpfSAAJQCAACCH26At6KcGiHMwrlHgQ',
    'y_0': 'CAACAgEAAxkBAALdjF_DweCfOggAAXv70jz-zPZEI1zoOwACUQgAAgh9ugIp6_QMB98hhh4E',
    'y_1': 'CAACAgEAAxkBAALdjl_DweGWuh-InhXrO915KxHMq801AAJSCAACCH26AnHYl4RX7ZdPHgQ',
    'y_2': 'CAACAgEAAxkBAALdkF_DweLYlWV9kykaFlSZBIJh4yO_AAJTCAACCH26AkLgAAEjqixVtR4E',
    'y_3': 'CAACAgEAAxkBAALdkl_DweOydkEzu1tYnNM62IJJRRwLAAJUCAACCH26Av-GLX4mBgi3HgQ',
    'y_4': 'CAACAgEAAxkBAALdlF_DweSzdYDzpWNBe31lE1jtztjJAAJVCAACCH26AsbMRQQ2nTqAHgQ',
    'y_5': 'CAACAgEAAxkBAALdll_DweUi670ZI1dQVL85Iy42pdbIAAJWCAACCH26ApUSyQJVJy0rHgQ',
    'y_6': 'CAACAgEAAxkBAALdmF_DwebtgBZFSpwF-wJD6eyBXMvUAAJXCAACCH26AlmpsEJr096LHgQ',
    'y_7': 'CAACAgEAAxkBAALdml_DwedVrlKKEuXaoBprRfhM_5CLAAJYCAACCH26Asx-fwgGUZ6UHgQ',
    'y_8': 'CAACAgEAAxkBAALdnF_DwejpMoArDN8SaVURxa5Sfe1pAAJZCAACCH26Ap5SGEQO1wdqHgQ',
    'y_9': 'CAACAgEAAxkBAALdnl_DwekW0JGSAAGLW9jAO-5WFnnp3wACWggAAgh9ugKcKeeYYyWHHh4E',
    'y_draw': 'CAACAgEAAxkBAALdoF_DweviLx-uS9kMoU_RTk97y545AAJbCAACCH26AvfIk9ubh8tVHgQ',
    'y_reverse': 'CAACAgEAAxkBAALdol_Dwez7XQt1t-Qvu0eVL7oDjbDaAAJcCAACCH26Au23XXEt8bDiHgQ',
    'y_skip': 'CAACAgEAAxkBAALdpF_Dwe1B-Y6s2NyP_A1XgxFCEtSmAAJdCAACCH26AgW7_Eo1ReRbHgQ',
    'colorchooser': 'CAACAgEAAxkBAALdpl_Dwe49a-XPlU3rZHEtojzzwDaKAAJeCAACCH26AiIryyOJYNhDHgQ',
    'draw_four': 'CAACAgEAAxkBAALdqF_Dwe-ZyDvDioFTFIxrslamO0gNAAJfCAACCH26AsWBCb6mlzs_HgQ'
}

class Card(object):
    """This class represents an UNO card"""

    def __init__(self, color, value, special=None):
        self.color = color
        self.value = value
        self.special = special

    def __str__(self):
        if self.special:
            return self.special
        else:
            return '%s_%s' % (self.color, self.value)

    def __repr__(self):
        if self.special:
            return '%s%s%s' % (COLOR_ICONS.get(self.color, ''),
                               COLOR_ICONS[BLACK],
                               ' '.join([s.capitalize()
                                         for s in self.special.split('_')]))
        else:
            return '%s%s' % (COLOR_ICONS[self.color], self.value.capitalize())

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)


def from_str(string):
    """Decodes a Card object from a string"""
    if string not in SPECIALS:
        color, value = string.split('_')
        return Card(color, value)
    else:
        return Card(None, None, string)
