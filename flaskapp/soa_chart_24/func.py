from ripe.atlas.cousteau import AtlasResultsRequest
from ripe.atlas.sagan import DnsResult
import datetime
import numpy as np
import plotly.graph_objects as go
import arrow


def get_plot(starttime, stoptime):


    kwargs_a = {
        "msm_id": 1413717,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_b = {
        "msm_id": 1413745,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_c = {
        "msm_id": 1413725,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_f = {
        "msm_id": 1413729,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_g = {
        "msm_id": 1413733,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_i = {
        "msm_id": 1413697,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_m ={
        "msm_id":24057751,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_x = {
        "msm_id": 6960402,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_y = {
        "msm_id": 11156555,
        "start": starttime,
        "stop": stoptime
    }
    kwargs_z = {
        "msm_id": 11156550,
        "start": starttime,
        "stop": stoptime
    }


    def create_list(kwargs):
        is_success, results = AtlasResultsRequest(**kwargs).create()
        if is_success:
            l_soa = []
            l_time = []
            l_dt = []
            l_hover = []
            count = 0
            while count < len(results)-1:
                my_error = DnsResult(results[count], on_error=DnsResult.ACTION_IGNORE)
                if not my_error.is_error:
                    timestamp = results[count]['timestamp']
                    dt = datetime.datetime.fromtimestamp(timestamp)
                    dt = dt.strftime("%m/%d/%Y , %H:%M:%S")
                    og_soa_serial = results[count]['result']['answers'][0]['SERIAL']
                    soa_serial = str(og_soa_serial)
                    soa_serial = datetime.datetime.strptime(soa_serial, "%Y%m%d%H")
                    soa_serial = datetime.datetime.timestamp(soa_serial)
                    l_soa.append(soa_serial)
                    l_time.append(timestamp)
                    l_dt.append(dt)
                    l_hover.append(og_soa_serial)
                count += 1
            return l_soa, l_time, l_dt, l_hover


    # Create a time list, soa list and datetime list for each measurement
    a = create_list(kwargs_a)
    b = create_list(kwargs_b)
    c = create_list(kwargs_c)
    f = create_list(kwargs_f)
    g = create_list(kwargs_g)
    i = create_list(kwargs_i)
    m = create_list(kwargs_m)
    x = create_list(kwargs_x)
    y = create_list(kwargs_y)
    z = create_list(kwargs_z)

    # Making a combined time/soa/datetime list for all servers
    all_soa_list = [a[0], b[0], c[0], f[0], g[0], i[0], m[0], x[0], y[0], z[0]]
    all_time_list = [a[1], b[1], c[1], f[1], g[1], i[1], m[1], x[1], y[1], z[1]]
    all_dt_list = [a[2], b[2], c[2], f[2], g[2], i[2], m[2], x[2], y[2], z[2]]
    hover_list = [a[3], b[3], c[3], f[3], g[3], i[3], m[3], x[3], y[3], z[3]]
    all_dt_list.sort()


    # Setting average datetime values
    for s in all_time_list:
        s.sort()
    av = [float(sum(l)) / len(l) for l in zip(*all_time_list)]
    timelist = []
    for count in av:
        dt = datetime.datetime.fromtimestamp(count)
        timelist.append(dt)

    # Setting colorbar tick values and tick text
    for item in all_soa_list:
        unique = np.unique(item)
        unique = list(unique)
    if len(unique) >= 40:
        unique=unique[0:-1:2]


    tickvals = unique
    ticktext = []
    for bla in unique:
        time = datetime.datetime.fromtimestamp(bla)
        time = datetime.datetime.strftime(time, '%Y%m%d%H')
        ticktext.append(time)


    # colorscale
    colorscalenums = []
    for i in np.arange(0, 1, 0.02):
        colorscalenums.append(i)

    colorscale = [
        [colorscalenums[0], '#87C38F'],
        [colorscalenums[1], '#87C38F'],
        [colorscalenums[1], '#226F54'],
        [colorscalenums[2], '#226F54'],
        [colorscalenums[2], '#291711'],
        [colorscalenums[3], '#291711'],
        [colorscalenums[3], '#95BF74'],
        [colorscalenums[4], '#95BF74'],
        [colorscalenums[4], '#659B5E'],
        [colorscalenums[5], '#659B5E'],
        [colorscalenums[5], '#A63D40'],
        [colorscalenums[6],'#A63D40'],
        [colorscalenums[6],'#DD2D4A'],
        [colorscalenums[7],'#DD2D4A'],
        [colorscalenums[7],'#F26A8D'],
        [colorscalenums[8],'#F26A8D'],
        [colorscalenums[8],'#F49CBB'],
        [colorscalenums[9],'#F49CBB'],
        [colorscalenums[9],'#904C77'],
        [colorscalenums[10],'#904C77'],
        [colorscalenums[10],'#5FAD56'],
        [colorscalenums[11],'#5FAD56'],
        [colorscalenums[11],'#F78154'],
        [colorscalenums[12], '#F78154'],
        [colorscalenums[12], '#F7EE7F'],
        [colorscalenums[13], '#F7EE7F'],
        [colorscalenums[13], '#4D9078'],
        [colorscalenums[14], '#4D9078'],
        [colorscalenums[14], '#B4436C'],
        [colorscalenums[15], '#B4436C'],
        [colorscalenums[15], '#29339B'],
        [colorscalenums[16], '#29339B'],
        [colorscalenums[16], '#74A4BC'],
        [colorscalenums[17], '#74A4BC'],
        [colorscalenums[17], '#1D3461'],
        [colorscalenums[18], '#1D3461'],
        [colorscalenums[18], '#1F487E'],
        [colorscalenums[19], '#1F487E'],
        [colorscalenums[19], '#247BA0'],
        [colorscalenums[20], '#247BA0'],
        [colorscalenums[20], '#2C0703'],
        [colorscalenums[21], '#2C0703'],
        [colorscalenums[21], '#890620'],
        [colorscalenums[22], '#890620'],
        [colorscalenums[22], '#B6465F'],
        [colorscalenums[23], '#B6465F'],
        [colorscalenums[23], '#DA9F93'],
        [colorscalenums[24], '#DA9F93'],
        [colorscalenums[24], '#EBD4CB'],
        [colorscalenums[25], '#EBD4CB'],
        [colorscalenums[25], '#ADFC92'],
        [colorscalenums[26], '#ADFC92'],
        [colorscalenums[26], '#4A0D67'],
        [colorscalenums[27], '#4A0D67'],
        [colorscalenums[27], '#473198'],
        [colorscalenums[28], '#473198'],
        [colorscalenums[28], '#9BF3F0'],
        [colorscalenums[29], '#9BF3F0'],
        [colorscalenums[29], '#DAFFED'],
        [colorscalenums[30], '#DAFFED'],
        [colorscalenums[30], '#2E382E'],
        [colorscalenums[31], '#2E382E'],
        [colorscalenums[31], '#50C9CE'],
        [colorscalenums[32], '#50C9CE'],
        [colorscalenums[32], '#72A1E5'],
        [colorscalenums[33], '#72A1E5'],
        [colorscalenums[33], '#9883E5'],
        [colorscalenums[34], '#9883E5'],
        [colorscalenums[34], '#FCD3DE'],
        [colorscalenums[35], '#FCD3DE'],
        [colorscalenums[35], '#B07156'],
        [colorscalenums[36], '#B07156'],
        [colorscalenums[36], '#AB4E68'],
        [colorscalenums[37], '#AB4E68'],
        [colorscalenums[37], '#533745'],
        [colorscalenums[38], '#533745'],
        [colorscalenums[38], '#9D9171'],
        [colorscalenums[39], '#9D9171'],
        [colorscalenums[39], '#C4A287'],
        [colorscalenums[40], '#C4A287'],
        [colorscalenums[40], '#DD403A'],
        [colorscalenums[41], '#DD403A'],
        [colorscalenums[41], '#B8B42D'],
        [colorscalenums[42], '#B8B42D'],
        [colorscalenums[42], '#3E363F'],
        [colorscalenums[43], '#3E363F'],
        [colorscalenums[43], '#FFFCE8'],
        [colorscalenums[44], '#FFFCE8'],
        [colorscalenums[44], '#697A21'],
        [colorscalenums[45], '#697A21'],
        [colorscalenums[45], '#06D6A0'],
        [colorscalenums[46], '#06D6A0'],
        [colorscalenums[46], '#1B9AAA'],
        [colorscalenums[47], '#1B9AAA'],
        [colorscalenums[47], '#EF476F'],
        [colorscalenums[48], '#EF476F'],
        [colorscalenums[48], '#FFC43D'],
        [colorscalenums[49], '#FFC43D'],
        [colorscalenums[49], '#DBFE87'],
        [1, '#DBFE87']
    ]
    # Creating plot, making a custom hovertemplate for the hovertext and editing the colorbar
        # Sorting soa values
    for i in all_soa_list:
        i.sort()

        # Define z, x, y and customdata values
    servers = ['a.ns.se', 'b.ns.se', 'c.ns.se', 'f.ns.se', 'g.ns.se', 'i.ns.se', 'm.ns.se', 'x.ns.se', 'y.ns.se', 'z.ns.se']
    z = all_soa_list
    time = timelist
    custom = all_dt_list
    text = hover_list

    fig = go.Figure(data=go.Heatmap(
            z=z,
            x=time,
            y=servers,
            text=text,
            customdata=custom,
            ygap=10,
            colorscale=colorscale,
            hovertemplate=
            "<b>SOA zones for .se</b><br><br>" +
            "<b>Server:</b> %{y}<br><br>" +
            "<b>Time:</b> %{customdata}<br><br>" +
            "<b>Soa zone:</b> %{text}<br><br>"
            "<extra></extra>",
            colorbar=dict(
                title='<b>SOA Zone<b>',
                tickfont=dict(
                family="arial",
                size=10,
                color="black"),
                showtickprefix="none",
                thickness=15,
                tickmode='array',
                tickvals=tickvals,
                ticktext=ticktext,
                lenmode='pixels',
                len=300,
            )
        )
        )

    # Updating some layout values
    fig.update_layout(
            template="ggplot2",
            title="SOA zones for .se secondary name servers from {0:%Y-%m-%d, %H:%M} to {1:%Y-%m-%d, %H:%M}".format(time[0], time[-1]),
            plot_bgcolor='white',
            xaxis=dict(
                title="Time",
                rangeslider=dict(visible=True, thickness=0.10),
                rangeselector=dict(
                buttons=list([
                    dict(count=3,
                         label="3 hours",
                         step="hour",
                         stepmode="backward"),
                    dict(count=12,
                         label="12 hours",
                         step="hour",
                         stepmode="backward"),
                    dict(count=24,
                         label="24 hours",
                         step="hour",
                         stepmode="todate"),
                    dict(count=48,
                         label="48 hours",
                         step="hour",
                         stepmode="backward"),
                    dict(step="all"),
            ]))),
            yaxis=dict(
                title="Server",
                autorange='reversed'
            ),
            autosize=True,
            font=dict(
                family="arial",
                size=13,
                color="black"),
            hoverlabel= dict(
                bgcolor='Black'
            )
            )


        # Write HTML file
    fig.write_html("templates/soagraph.html")
