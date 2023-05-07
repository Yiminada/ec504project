import setupVRP as vrp
import plotly.graph_objects as go

def make_annotations(pos, text, font_size=10, font_color='rgb(250,250,250)'):
    L=len(pos)
    if len(text)!=L:
        raise ValueError('The lists pos and text must have the same len')
    annotations = []
    for k in range(L):
        annotations.append(
            dict(
                text=text[k], # or replace labels with a different list for the text within the circle
                x=pos[k][0], y=pos[k][1],
                xref='x1', yref='y1',
                font=dict(color=font_color, size=font_size),
                showarrow=False)
        )
    return annotations

def showMap(edges=None,fig=None,printFlag=False,title="",edgeColor='gray'):
    if edges is None and fig is not None:
        fig.show()
        return

    Xe = []
    Ye = []
    Xn = []
    Yn = []
    M = max([edge[0].ycoords for edge in edges])
    for edge in edges:
        Xe += [edge[0].xcoords,edge[1].xcoords,None]
        Ye += [edge[0].ycoords,edge[1].ycoords,None]
        Xn += [edge[0].xcoords]
        Yn += [edge[0].ycoords]

    labels = [edge[0].id for edge in edges]
    if fig is None:
        fig = go.Figure()
        printFlag = True
    
    fig.add_trace(go.Scatter(x=Xe,
                    y=Ye,
                    mode='lines',
                    line=dict(color=edgeColor, width=1),
                    hoverinfo='none'
                    ))
    fig.add_trace(go.Scatter(x=Xn,
                    y=Yn,
                    mode='markers',
                    name='bla',
                    marker=dict(symbol='circle-dot',
                                    size=18,
                                    color='#6175c1',    #'#DB4551',
                                    line=dict(color='rgb(50,50,50)', width=1)
                                    ),
                    text=labels,
                    hoverinfo='text',
                    opacity=0.8
                    ))
    fig.add_trace(go.Scatter(x=[Xn[0]],
                             y=[Yn[0]],
                             mode='markers',
                             name='orig',
                             marker=dict(symbol='circle-dot',
                                         size=18,
                                         color='#33E833',
                                         line=dict(color='rgb(50,50,50)',width=1)),
                             text=[labels[0]],
                             hoverinfo='text',
                             opacity=0.8))
    
    axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                )
    position = [(edge[0].xcoords,edge[0].ycoords) for edge in edges]
    fig.update_layout(title=title,
                annotations=make_annotations(position, labels),
                font_size=12,
                showlegend=False,
                xaxis=axis,
                yaxis=axis,
                margin=dict(l=40, r=40, b=85, t=100),
                hovermode='closest',
                plot_bgcolor='rgb(248,248,248)'
                )
    
    if printFlag:
        fig.show()
    return fig


if __name__ == "__main__":
    client1 = vrp.client(0, 1, 10, 20, 504, 207, 90)
    client2 = vrp.client(1, 2, 1, 3, 504, 207, 90)
    v1 = vrp.vehicle(0,100)
    r = vrp.route(client1,v1)
    r.Insert(client2, client1)

    client3 = vrp.client(2, 2, 3, 3, 504, 207, 90)
    r.Insert(client3,client1)
    
    client4 = vrp.client(3, 1.5, 7, 3, 504, 207, 90)
    r.Insert(client4,client1)

    showMap(r.edges,title="Test Tree")
