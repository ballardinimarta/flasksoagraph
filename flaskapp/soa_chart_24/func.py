from ripe.atlas.cousteau import AtlasResultsRequest
from ripe.atlas.sagan import DnsResult
import datetime
import numpy as np
import plotly.graph_objects as go



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
            count = 0
            while count < len(results)-1:
                my_error = DnsResult(results[count], on_error=DnsResult.ACTION_IGNORE)
                if not my_error.is_error:
                    timestamp = results[count]['timestamp']
                    dt = datetime.datetime.fromtimestamp(timestamp)
                    dt = dt.strftime("%m/%d/%Y , %H:%M:%S")
                    soa_serial = results[count]['result']['answers'][0]['SERIAL']
                    soa_serial = str(soa_serial)
                    soa_serial = datetime.datetime.strptime(soa_serial, "%Y%m%d%H")
                    soa_serial = datetime.datetime.timestamp(soa_serial)
                    l_soa.append(soa_serial)
                    l_time.append(timestamp)
                    l_dt.append(dt)
                count += 1
            return l_soa, l_time, l_dt


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

    tickvals = unique
    ticktext = []
    for bla in unique:
        time = datetime.datetime.fromtimestamp(bla)
        time = datetime.datetime.strftime(time, '%Y%m%d%H')
        ticktext.append(time)

    # colorscale

    colorscalenums = []
    for i in np.arange(0, 1, 0.03333333):
        colorscalenums.append(i)

    colorscale = [
        [colorscalenums[0], '#d1a99a'],
        [colorscalenums[1], '#d1a99a'],
        [colorscalenums[1], '#8d236d'],
        [colorscalenums[2], '#8d236d'],
        [colorscalenums[2], '#c8d62e'],
        [colorscalenums[3], '#c8d62e'],
        [colorscalenums[3], '#f4c625'],
        [colorscalenums[4], '#f4c625'],
        [colorscalenums[4], '#a8f030'],
        [colorscalenums[5], '#a8f030'],
        [colorscalenums[5], '#55ca61'],
        [colorscalenums[6],'#55ca61'],
        [colorscalenums[6],'#a79d79'],
        [colorscalenums[7],'#a79d79'],
        [colorscalenums[7],'#1ee481'],
        [colorscalenums[8],'#1ee481'],
        [colorscalenums[8],'#452529'],
        [colorscalenums[9],'#452529'],
        [colorscalenums[9],'#bd3bc4'],
        [colorscalenums[10],'#bd3bc4'],
        [colorscalenums[10],'#0cfbd9'],
        [colorscalenums[11],'#0cfbd9'],
        [colorscalenums[11],'#3b2df5'],
        [colorscalenums[12], '#3b2df5'],
        [colorscalenums[12], '#73303c'],
        [colorscalenums[13], '#73303c'],
        [colorscalenums[13], '#dbb0c3'],
        [colorscalenums[14], '#dbb0c3'],
        [colorscalenums[14], '#81f5b3'],
        [colorscalenums[15], '#81f5b3'],
        [colorscalenums[15], '#38b913'],
        [colorscalenums[16], '#38b913'],
        [colorscalenums[16], '#93c5ae'],
        [colorscalenums[17], '#93c5ae'],
        [colorscalenums[17], '#d8b13b'],
        [colorscalenums[18], '#d8b13b'],
        [colorscalenums[18], '#e8a521'],
        [colorscalenums[19], '#e8a521'],
        [colorscalenums[19], '#fefa30'],
        [colorscalenums[20], '#fefa30'],
        [colorscalenums[20], '#483521'],
        [colorscalenums[21], '#483521'],
        [colorscalenums[21], '#c070e7'],
        [colorscalenums[22], '#c070e7'],
        [colorscalenums[22], '#ebf963'],
        [colorscalenums[23], '#ebf963'],
        [colorscalenums[23], '#9c9046'],
        [colorscalenums[24], '#9c9046'],
        [colorscalenums[24], '#2994cd'],
        [colorscalenums[25], '#2994cd'],
        [colorscalenums[25], '#f80f48'],
        [colorscalenums[26], '#f80f48'],
        [colorscalenums[26], '#8d9bed'],
        [colorscalenums[27], '#8d9bed'],
        [colorscalenums[27], '#8ac4bd'],
        [colorscalenums[28], '#8ac4bd'],
        [colorscalenums[28], '#ebd060'],
        [colorscalenums[29], '#ebd060'],
        [colorscalenums[29], '#d1da59'],
        [1, '#d1da59'],

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

    fig = go.Figure(data=go.Heatmap(
            z=z,
            x=time,
            y=servers,
            customdata=custom,
            ygap=10,
            colorscale=colorscale,
            hovertemplate=
            "<b>SOA zones for .se</b><br><br>" +
            "<b>Server:</b> %{y}<br><br>" +
            "<b>Time:</b> %{customdata}<br><br>" +
            "<b>Soa zone:</b> %{z}<br><br>"
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
            )
        )
        )
        # Updating some layout values
    fig.update_layout(
            template="ggplot2",
            title="SOA zones for .se secondary name servers",
            plot_bgcolor='white',
            xaxis=dict(
                title="Time",
                rangeslider=dict(visible=True, thickness=0.10),
                rangeselector=dict(
                    buttons=list([
                        dict(count=30,
                             label="30 min",
                             step="minute",
                             stepmode="backward"),
                        dict(count=1,
                             label="1 hour",
                             step="hour",
                             stepmode="backward"),
                        dict(count=2,
                             label="2 hour",
                             step="hour",
                             stepmode="backward"),
                        dict(count=3,
                             label="3 hour",
                             step="hour",
                             stepmode="backward"),
                        dict(step="all")
                    ])
                ),
            ),
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
    fig.write_html("<path to your directory>/flasksoagraph/flaskapp/templates/soagraph.html")
