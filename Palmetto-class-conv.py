#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        # add nodes, switches first...
        RockHill = self.addSwitch( 's0' )
        Charlotte = self.addSwitch( 's1' )
        Bethune = self.addSwitch( 's2' )
        Lancaster = self.addSwitch( 's3' )
        Courtney = self.addSwitch( 's4' )
        Lexington = self.addSwitch( 's5' )
        Concord = self.addSwitch( 's6' )
        Salisbury = self.addSwitch( 's7' )
        HighPoint = self.addSwitch( 's8' )
        Asheboro = self.addSwitch( 's9' )
        Orangeburg = self.addSwitch( 's10' )
        Aiken = self.addSwitch( 's11' )
        Chester = self.addSwitch( 's12' )
        Columbia = self.addSwitch( 's13' )
        Sumter = self.addSwitch( 's14' )
        Georgetown = self.addSwitch( 's15' )
        MoncksCorner = self.addSwitch( 's16' )
        Charleston = self.addSwitch( 's17' )
        StGeorge = self.addSwitch( 's18' )
        Walterboro = self.addSwitch( 's19' )
        Yemassee = self.addSwitch( 's20' )
        Augusta = self.addSwitch( 's21' )
        HiltonHead = self.addSwitch( 's22' )
        Beaufort = self.addSwitch( 's23' )
        Savannah = self.addSwitch( 's24' )
        Greenwood = self.addSwitch( 's25' )
        DueWest = self.addSwitch( 's26' )
        Spartanburg = self.addSwitch( 's27' )
        Asheville = self.addSwitch( 's28' )
        Boone = self.addSwitch( 's29' )
        Hickory = self.addSwitch( 's30' )
        Anderson = self.addSwitch( 's31' )
        Clemson = self.addSwitch( 's32' )
        Toccoa = self.addSwitch( 's33' )
        Greenville = self.addSwitch( 's34' )
        MyrtleBeach = self.addSwitch( 's35' )
        Florence = self.addSwitch( 's36' )
        Baldwin = self.addSwitch( 's37' )
        Sparta = self.addSwitch( 's38' )
        LevelCross = self.addSwitch( 's39' )
        Greensboro = self.addSwitch( 's40' )
        Raleigh = self.addSwitch( 's41' )
        RockyMount = self.addSwitch( 's42' )
        Fayetteville = self.addSwitch( 's43' )
        Wilmington = self.addSwitch( 's44' )

        # ... and now hosts
        RockHill_host = self.addHost( 'h0' )
        Charlotte_host = self.addHost( 'h1' )
        Bethune_host = self.addHost( 'h2' )
        Lancaster_host = self.addHost( 'h3' )
        Courtney_host = self.addHost( 'h4' )
        Lexington_host = self.addHost( 'h5' )
        Concord_host = self.addHost( 'h6' )
        Salisbury_host = self.addHost( 'h7' )
        HighPoint_host = self.addHost( 'h8' )
        Asheboro_host = self.addHost( 'h9' )
        Orangeburg_host = self.addHost( 'h10' )
        Aiken_host = self.addHost( 'h11' )
        Chester_host = self.addHost( 'h12' )
        Columbia_host = self.addHost( 'h13' )
        Sumter_host = self.addHost( 'h14' )
        Georgetown_host = self.addHost( 'h15' )
        MoncksCorner_host = self.addHost( 'h16' )
        Charleston_host = self.addHost( 'h17' )
        StGeorge_host = self.addHost( 'h18' )
        Walterboro_host = self.addHost( 'h19' )
        Yemassee_host = self.addHost( 'h20' )
        Augusta_host = self.addHost( 'h21' )
        HiltonHead_host = self.addHost( 'h22' )
        Beaufort_host = self.addHost( 'h23' )
        Savannah_host = self.addHost( 'h24' )
        Greenwood_host = self.addHost( 'h25' )
        DueWest_host = self.addHost( 'h26' )
        Spartanburg_host = self.addHost( 'h27' )
        Asheville_host = self.addHost( 'h28' )
        Boone_host = self.addHost( 'h29' )
        Hickory_host = self.addHost( 'h30' )
        Anderson_host = self.addHost( 'h31' )
        Clemson_host = self.addHost( 'h32' )
        Toccoa_host = self.addHost( 'h33' )
        Greenville_host = self.addHost( 'h34' )
        MyrtleBeach_host = self.addHost( 'h35' )
        Florence_host = self.addHost( 'h36' )
        Baldwin_host = self.addHost( 'h37' )
        Sparta_host = self.addHost( 'h38' )
        LevelCross_host = self.addHost( 'h39' )
        Greensboro_host = self.addHost( 'h40' )
        Raleigh_host = self.addHost( 'h41' )
        RockyMount_host = self.addHost( 'h42' )
        Fayetteville_host = self.addHost( 'h43' )
        Wilmington_host = self.addHost( 'h44' )

        # add edges between switch and corresponding host
        self.addLink( RockHill , RockHill_host )
        self.addLink( Charlotte , Charlotte_host )
        self.addLink( Bethune , Bethune_host )
        self.addLink( Lancaster , Lancaster_host )
        self.addLink( Courtney , Courtney_host )
        self.addLink( Lexington , Lexington_host )
        self.addLink( Concord , Concord_host )
        self.addLink( Salisbury , Salisbury_host )
        self.addLink( HighPoint , HighPoint_host )
        self.addLink( Asheboro , Asheboro_host )
        self.addLink( Orangeburg , Orangeburg_host )
        self.addLink( Aiken , Aiken_host )
        self.addLink( Chester , Chester_host )
        self.addLink( Columbia , Columbia_host )
        self.addLink( Sumter , Sumter_host )
        self.addLink( Georgetown , Georgetown_host )
        self.addLink( MoncksCorner , MoncksCorner_host )
        self.addLink( Charleston , Charleston_host )
        self.addLink( StGeorge , StGeorge_host )
        self.addLink( Walterboro , Walterboro_host )
        self.addLink( Yemassee , Yemassee_host )
        self.addLink( Augusta , Augusta_host )
        self.addLink( HiltonHead , HiltonHead_host )
        self.addLink( Beaufort , Beaufort_host )
        self.addLink( Savannah , Savannah_host )
        self.addLink( Greenwood , Greenwood_host )
        self.addLink( DueWest , DueWest_host )
        self.addLink( Spartanburg , Spartanburg_host )
        self.addLink( Asheville , Asheville_host )
        self.addLink( Boone , Boone_host )
        self.addLink( Hickory , Hickory_host )
        self.addLink( Anderson , Anderson_host )
        self.addLink( Clemson , Clemson_host )
        self.addLink( Toccoa , Toccoa_host )
        self.addLink( Greenville , Greenville_host )
        self.addLink( MyrtleBeach , MyrtleBeach_host )
        self.addLink( Florence , Florence_host )
        self.addLink( Baldwin , Baldwin_host )
        self.addLink( Sparta , Sparta_host )
        self.addLink( LevelCross , LevelCross_host )
        self.addLink( Greensboro , Greensboro_host )
        self.addLink( Raleigh , Raleigh_host )
        self.addLink( RockyMount , RockyMount_host )
        self.addLink( Fayetteville , Fayetteville_host )
        self.addLink( Wilmington , Wilmington_host )

        # add edges between switches
        self.addLink( RockHill , Charlotte, bw=10, delay='0.19038018985ms')
        self.addLink( RockHill , Charlotte, bw=10, delay='0.19038018985ms')
        self.addLink( RockHill , Lancaster, bw=10, delay='0.165070696006ms')
        self.addLink( RockHill , Chester, bw=10, delay='0.152179762294ms')
        self.addLink( Charlotte , Spartanburg, bw=10, delay='0.527348642307ms')
        self.addLink( Charlotte , Concord, bw=10, delay='0.159095386113ms')
        self.addLink( Bethune , Lancaster, bw=10, delay='0.261551098098ms')
        self.addLink( Bethune , Florence, bw=10, delay='0.300378343317ms')
        self.addLink( Bethune , Sumter, bw=10, delay='0.27941530441ms')
        self.addLink( Courtney , LevelCross, bw=10, delay='0.248231981487ms')
        self.addLink( Courtney , Baldwin, bw=10, delay='0.446557502859ms')
        self.addLink( Courtney , Lexington, bw=10, delay='0.214540164387ms')
        self.addLink( Courtney , Lexington, bw=10, delay='0.214540164387ms')
        self.addLink( Lexington , HighPoint, bw=10, delay='0.135760125987ms')
        self.addLink( Lexington , Asheboro, bw=10, delay='0.212032019707ms')
        self.addLink( Lexington , Concord, bw=10, delay='0.278407808291ms')
        self.addLink( Lexington , Salisbury, bw=10, delay='0.139942886385ms')
        self.addLink( Concord , Salisbury, bw=10, delay='0.143270541339ms')
        self.addLink( HighPoint , Greensboro, bw=10, delay='0.117795586955ms')
        self.addLink( HighPoint , Asheboro, bw=10, delay='0.16527290506ms')
        self.addLink( Orangeburg , StGeorge, bw=10, delay='0.217567894146ms')
        self.addLink( Orangeburg , Columbia, bw=10, delay='0.299628364087ms')
        self.addLink( Aiken , Augusta, bw=10, delay='0.120322045744ms')
        self.addLink( Aiken , Columbia, bw=10, delay='0.406604815013ms')
        self.addLink( Chester , DueWest, bw=10, delay='0.585342555094ms')
        self.addLink( Chester , Columbia, bw=10, delay='0.40660763331ms')
        self.addLink( Columbia , Augusta, bw=10, delay='0.520119719121ms')
        self.addLink( Columbia , Sumter, bw=10, delay='0.328107410704ms')
        self.addLink( Sumter , MoncksCorner, bw=10, delay='0.437584031059ms')
        self.addLink( Sumter , Florence, bw=10, delay='0.312401431321ms')
        self.addLink( Sumter , Georgetown, bw=10, delay='0.580430941016ms')
        self.addLink( Georgetown , MyrtleBeach, bw=10, delay='0.260819409279ms')
        self.addLink( MoncksCorner , Charleston, bw=10, delay='0.24019137022ms')
        self.addLink( Charleston , Savannah, bw=10, delay='0.681297623507ms')
        self.addLink( Charleston , StGeorge, bw=10, delay='0.383304470867ms')
        self.addLink( Charleston , MyrtleBeach, bw=10, delay='0.713762848571ms')
        self.addLink( StGeorge , Walterboro, bw=10, delay='0.164454259312ms')
        self.addLink( Walterboro , Yemassee, bw=10, delay='0.149626441573ms')
        self.addLink( Yemassee , Savannah, bw=10, delay='0.362830155332ms')
        self.addLink( Yemassee , HiltonHead, bw=10, delay='0.271816654297ms')
        self.addLink( Yemassee , Beaufort, bw=10, delay='0.169617920355ms')
        self.addLink( Yemassee , Beaufort, bw=10, delay='0.169617920355ms')
        self.addLink( Augusta , Savannah, bw=10, delay='0.900667623351ms')
        self.addLink( Augusta , Anderson, bw=10, delay='0.650632935882ms')
        self.addLink( HiltonHead , Savannah, bw=10, delay='0.182276920773ms')
        self.addLink( Greenwood , DueWest, bw=10, delay='0.131283818646ms')
        self.addLink( Greenwood , DueWest, bw=10, delay='0.131283818646ms')
        self.addLink( DueWest , Anderson, bw=10, delay='0.155463654717ms')
        self.addLink( Spartanburg , Greenville, bw=10, delay='0.22098869513ms')
        self.addLink( Spartanburg , Hickory, bw=10, delay='0.519850432561ms')
        self.addLink( Asheville , Greenville, bw=10, delay='0.429263221723ms')
        self.addLink( Asheville , Hickory, bw=10, delay='0.561765268237ms')
        self.addLink( Boone , Baldwin, bw=10, delay='0.0981318899728ms')
        self.addLink( Boone , Baldwin, bw=10, delay='0.0981318899728ms')
        self.addLink( Anderson , Clemson, bw=10, delay='0.133909225818ms')
        self.addLink( Anderson , Toccoa, bw=10, delay='0.320300660619ms')
        self.addLink( Clemson , Toccoa, bw=10, delay='0.237848634126ms')
        self.addLink( Clemson , Greenville, bw=10, delay='0.226922817216ms')
        self.addLink( Toccoa , Greenville, bw=10, delay='0.462792978544ms')
        self.addLink( MyrtleBeach , Florence, bw=10, delay='0.500458533008ms')
        self.addLink( MyrtleBeach , Florence, bw=10, delay='0.500458533008ms')
        self.addLink( MyrtleBeach , Wilmington, bw=10, delay='0.535621106262ms')
        self.addLink( Florence , Fayetteville, bw=10, delay='0.635356546039ms')
        self.addLink( Baldwin , Sparta, bw=10, delay='0.207442119893ms')
        self.addLink( Sparta , LevelCross, bw=10, delay='0.233328568173ms')
        self.addLink( Greensboro , Raleigh, bw=10, delay='0.554432026936ms')
        self.addLink( Raleigh , RockyMount, bw=10, delay='0.395153506953ms')
        self.addLink( Raleigh , Fayetteville, bw=10, delay='0.421263216838ms')
        self.addLink( RockyMount , Fayetteville, bw=10, delay='0.700320778342ms')
        self.addLink( Fayetteville , Wilmington, bw=10, delay='0.637770426137ms')

topos = { 'generated': ( lambda: GeneratedTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vm
controller_ip = ''

def setupNetwork(controller_ip):
    "Create network and run simple performance test"
    # check if remote controller's ip was set
    # else set it to localhost
    topo = GeneratedTopo()
    if controller_ip == '':
        #controller_ip = '10.0.2.2';
        controller_ip = '127.0.0.1';
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
    info( '*** Adding controller\n' )  
     
    c0=net.addController(name='c0',  
            controller=RemoteController,  
            ip='127.0.0.1',  
            port=6633)  
     
    c1=net.addController(name='c1',  
            controller=RemoteController,  
            ip='127.0.0.2',  
            port=6634)  
    c2=net.addController(name='c2',  
            controller=RemoteController,  
            ip='127.0.0.3',  
            port=6635)  
    c3=net.addController(name='c3',  
            controller=RemoteController,  
            ip='4',  
            port=6636)  
    # Connect each switch to a different controller
    net.get('s0').start([c1])
    net.get('s1').start([c1])
    net.get('s2').start([c0])
    net.get('s3').start([c1])
    net.get('s4').start([c1])
    net.get('s5').start([c1])
    net.get('s6').start([c1])
    net.get('s7').start([c1])
    net.get('s8').start([c1])
    net.get('s9').start([c1])
    net.get('s10').start([c0])
    net.get('s11').start([c2])
    net.get('s12').start([c2])
    net.get('s13').start([c0])
    net.get('s14').start([c0])
    net.get('s15').start([c0])
    net.get('s16').start([c0])
    net.get('s17').start([c0])
    net.get('s18').start([c0])
    net.get('s19').start([c0])
    net.get('s20').start([c0])
    net.get('s21').start([c2])
    net.get('s22').start([c0])
    net.get('s23').start([c0])
    net.get('s24').start([c0])
    net.get('s25').start([c2])
    net.get('s26').start([c2])
    net.get('s27').start([c2])
    net.get('s28').start([c2])
    net.get('s29').start([c1])
    net.get('s30').start([c1])
    net.get('s31').start([c2])
    net.get('s32').start([c2])
    net.get('s33').start([c2])
    net.get('s34').start([c2])
    net.get('s35').start([c3])
    net.get('s36').start([c0])
    net.get('s37').start([c1])
    net.get('s38').start([c1])
    net.get('s39').start([c1])
    net.get('s40').start([c1])
    net.get('s41').start([c3])
    net.get('s42').start([c3])
    net.get('s43').start([c3])
    net.get('s44').start([c3])
 
    return net

def connectToRootNS( network, switch, ip, prefixLen, routes ):
    "Connect hosts to root namespace via switch. Starts network."
    "network: Mininet() network object"
    "switch: switch to connect to root namespace"
    "ip: IP address for root namespace node"
    "prefixLen: IP address prefix length (e.g. 8, 16, 24)"
    "routes: host networks to route to"
    # Create a node in root namespace and link to switch 0
    root = Node( 'root', inNamespace=False )
    intf = TCLink( root, switch ).intf1
    root.setIP( ip, prefixLen, intf )
    # Start network that now includes link to root namespace
    network.start()
    # Add routes from root ns to hosts
    for route in routes:
        root.cmd( 'route add -net ' + route + ' dev ' + str( intf ) )

def sshd( network, cmd='/usr/sbin/sshd', opts='-D' ):
    "Start a network, connect it to root ns, and run sshd on all hosts."
    switch = network.switches[ 0 ]  # switch to use
    ip = '10.123.123.1'  # our IP address on host network
    routes = [ '10.0.0.0/8' ]  # host networks to route to
    connectToRootNS( network, switch, ip, 8, routes )
    for host in network.hosts:
        host.cmd( cmd + ' ' + opts + '&' )

    # DEBUGGING INFO
    print
    print "Dumping host connections"
    dumpNodeConnections(network.hosts)
    print
    print "*** Hosts are running sshd at the following addresses:"
    print
    for host in network.hosts:
        print host.name, host.IP()
    print
    print "*** Type 'exit' or control-D to shut down network"
    print
    print "*** For testing network connectivity among the hosts, wait a bit for the controller to create all the routes, then do 'pingall' on the mininet console."
    print

    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )
    network.stop()


if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    sshd( setupNetwork(controller_ip) )
