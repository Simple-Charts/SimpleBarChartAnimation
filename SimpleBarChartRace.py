import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
import sys
from tqdm import tqdm

data_file = 'covid19_new_cases.csv'
title = 'COVID-19 New Cases'
title_fontsize = 10
footnote1 = 'Data Source: https://github.com/owid/covid-19-data'
footnote2 = 'Source Code: https://github.com/Simple-Charts/SimpleBarChartRace'
footnote_fontsize = 4
xlabel_text = ''
xlabel_fontsize = 5
tick_fontsize = 5
tick_offset_fontsize = 6
fontname = "Meiryo"
time_fontsize = 16
frames = 5
ranks = 15
image_dpi = 300
video_height = 500
video_width = 800
video_fps = 15

if not os.path.exists("image"):
    os.mkdir("image")
df = pd.read_csv(data_file)
df = df.fillna(0)
df.index = df.index * frames
df_value = df.reindex(range((len(df)-1)*frames+1))
df_value['date'] = df_value['date'].fillna(method='ffill')
df_value = df_value.set_index('date')
df_rank = df_value.rank(axis=1, method='first')
df_value = df_value.interpolate()
for i in range(len(df_value)):
    zero_value = df_value.iloc[i].index[df_value.iloc[i] == 0.0]
    df_rank.iloc[i][zero_value] = 0
df_rank = df_rank.interpolate()
labels = df_value.columns
colors = plt.cm.Paired(range(12))

for i in tqdm(range(len(df_value))):
    fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
    plt.rcParams["font.family"] = fontname 
    ax.barh(y = df_rank.iloc[i], width = df_value.iloc[i], color = colors, tick_label = labels)
    ax.set_xlabel(xlabel_text, fontsize = xlabel_fontsize)
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.tick_params(axis='x', labelsize = tick_fontsize)
    ax.tick_params(axis='y', labelsize = tick_fontsize)
    ax.ticklabel_format(style="sci", axis="x", scilimits=(0,0))
    #ax.xaxis.get_offset_text().set_fontsize(tick_offset_fontsize)
    ax.xaxis.get_offset_text().set_visible(False)
    plt.tight_layout()
    offset = ax.xaxis.get_offset_text().get_text()[2:]
    ax.text(1, 1.2, "x" + rf"$10^{{{str(offset)}}}$", va='top', ha='right', transform=ax.transAxes, fontsize = tick_offset_fontsize)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]
    ax.set_ylim(len(labels) - (ranks - 0.5), len(labels) + 0.5)
    ax.set_xlim(0,)
    plt.subplots_adjust(left=0.35, right=0.9, bottom=0.1, top=0.7)
    plt.suptitle(title, y=0.95, fontsize = title_fontsize)
    ax.text(1, -0.1, df_value.index[i], transform = ax.transAxes, size = time_fontsize, ha='right', weight=750)
    ax.text(-0.6, -0.1, footnote1, transform = ax.transAxes, size = footnote_fontsize, ha='left')
    ax.text(-0.6, -0.14, footnote2, transform = ax.transAxes, size = footnote_fontsize, ha='left')
    plt.savefig("image/img"+str(i).zfill(4)+".png", dpi=image_dpi)

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter('video.mp4', fourcc, fps = video_fps, frameSize = (video_width, video_height))
for i in tqdm(range(len(df_value))):
    img = cv2.imread('image/img%04d.png' % i)
    img = cv2.resize(img, (video_width, video_height))
    video.write(img)
video.release()
