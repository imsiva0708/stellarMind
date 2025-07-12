// import React, { useEffect, useState } from 'react';
// import { Shield, Battery, Wifi, Cpu, Timer, AlertTriangle, TrendingUp, TrendingDown } from 'lucide-react';
// import { DataService } from '../services/dataService';
// import SatelliteOrbit from './visualizations/SatelliteOrbit';
// import TelemetryGraphs from './visualizations/TelemetryGraphs';
// import MissionTimeline from './visualizations/MissionTimeline';
// import ResourceHeatmap from './visualizations/ResourceHeatmap';

// const dataService = new DataService();

// const Dashboard = () => {
//   const [systemStatus, setSystemStatus] = useState<any>(null);
//   const [performanceData, setPerformanceData] = useState<any[]>([]);
//   const [tasks, setTasks] = useState<any[]>([]);
//   const [trends, setTrends] = useState<any>({
//     power: 0,
//     battery: 0,
//     storage: 0
//   });
//   const [resourceHeatmapData, setResourceHeatmapData] = useState<any[]>([]);

//   useEffect(() => {
//     const initializeData = async () => {
//       await dataService.loadData();
//       updateData();
//       generateHeatmapData();
//     };

//     const updateData = () => {
//       const status = dataService.getLatestSystemStatus();
//       const performance = dataService.getSystemPerformanceData();
//       const activeTasks = dataService.getActiveTasks();

//       setSystemStatus(status);
//       setPerformanceData(performance);
//       setTasks(activeTasks);

//       if (performance.length >= 2) {
//         const latest = performance[0];
//         const previous = performance[1];
//         setTrends({
//           power: latest.power - previous.power,
//           battery: latest.battery - previous.battery,
//           storage: latest.storage - previous.storage
//         });
//       }
//     };

//     const generateHeatmapData = () => {
//       // Generate sample resource usage data for the heatmap
//       const data = [];
//       for (let day = 0; day < 7; day++) {
//         for (let hour = 0; hour < 24; hour++) {
//           data.push({
//             day,
//             hour,
//             value: 30 + Math.random() * 70 // Random resource usage between 30-100%
//           });
//         }
//       }
//       setResourceHeatmapData(data);
//     };

//     initializeData();
//     const refreshInterval = setInterval(updateData, 1000);

//     return () => {
//       clearInterval(refreshInterval);
//     };
//   }, []);

//   if (!systemStatus) return <div>Loading...</div>;

//   const stats = [
//     { 
//       icon: Shield, 
//       label: 'System Status', 
//       value: systemStatus.health.propulsion === 'Operational' ? 'Nominal' : 'Warning',
//       color: systemStatus.health.propulsion === 'Operational' ? 'text-green-500' : 'text-yellow-500',
//       trend: null
//     },
//     { 
//       icon: Battery, 
//       label: 'Power', 
//       value: `${Math.round(systemStatus.power.batteryLevel)}%`,
//       color: 'text-blue-500',
//       trend: trends.battery
//     },
//     { 
//       icon: Wifi, 
//       label: 'Signal Strength',
//       value: systemStatus.health.communication === 'Stable' ? 'Strong' : 'Weak',
//       color: systemStatus.health.communication === 'Stable' ? 'text-purple-500' : 'text-red-500',
//       trend: null
//     },
//     { 
//       icon: Cpu, 
//       label: 'Storage',
//       value: `${Math.round(systemStatus.storage)} MB`,
//       color: 'text-orange-500',
//       trend: trends.storage
//     },
//   ];

//   const handleTasksReorder = (newTasks: any[]) => {
//     setTasks(newTasks);
//   };

//   return (
//     <div className="space-y-6">
//       {/* Status Cards */}
//       <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
//         {stats.map((stat, index) => (
//           <div key={index} className="bg-white rounded-lg shadow-lg p-6 transform hover:scale-105 transition-transform duration-200">
//             <div className="flex items-center justify-between">
//               <div className="flex items-center">
//                 <stat.icon className={`h-8 w-8 ${stat.color}`} />
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-600">{stat.label}</p>
//                   <p className="text-2xl font-semibold">{stat.value}</p>
//                 </div>
//               </div>
//               {stat.trend !== null && (
//                 <div className={`flex items-center ${stat.trend >= 0 ? 'text-green-500' : 'text-red-500'}`}>
//                   {stat.trend >= 0 ? <TrendingUp className="h-5 w-5" /> : <TrendingDown className="h-5 w-5" />}
//                   <span className="ml-1 text-sm">{Math.abs(stat.trend).toFixed(1)}%</span>
//                 </div>
//               )}
//             </div>
//           </div>
//         ))}
//       </div>

//       {/* 3D Visualization and Telemetry */}
//       <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
//         <div className="bg-white rounded-lg shadow-lg p-6">
//           <h3 className="text-lg font-semibold mb-4">Satellite Orbit Visualization</h3>
//           <SatelliteOrbit satelliteData={[{
//             orbital_position_x_km: systemStatus.orbital_position_x || 0,
//             orbital_position_y_km: systemStatus.orbital_position_y || 0,
//             orbital_position_z_km: systemStatus.orbital_position_z || 0
//           }]} />
//         </div>
//         <div>
//           <TelemetryGraphs data={performanceData} />
//         </div>
//       </div>

//       {/* Mission Timeline and Resource Heatmap */}
//       <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
//         <MissionTimeline tasks={tasks} onTasksReorder={handleTasksReorder} />
//         <ResourceHeatmap
//           data={resourceHeatmapData}
//           title="Resource Usage Pattern"
//           colorScale={['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#084594']}
//         />
//       </div>
//     </div>
//   );
// };

// export default Dashboard;
import React, { useEffect, useState } from 'react';
import { Shield, Battery, Wifi, Cpu, Thermometer, HardDrive, AlertTriangle, TrendingUp, TrendingDown, Sun } from 'lucide-react';
import SatelliteOrbit from './visualizations/SatelliteOrbit';
import TelemetryGraphs from './visualizations/TelemetryGraphs';
import MissionTimeline from './visualizations/MissionTimeline';
import ResourceHeatmap from './visualizations/ResourceHeatmap';

const Dashboard = () => {
  const [systemData, setSystemData] = useState<any>(null);

  useEffect(() => {
    const ws = new WebSocket("ws://127.0.0.1:8000/ws");

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setSystemData(data);
    };

    ws.onclose = () => console.log("WebSocket Disconnected");
    ws.onerror = (error) => console.log("WebSocket Error: ", error);

    return () => {
      ws.close();
    };
  }, []);

  if (!systemData) return <div>Loading...</div>;

  const stats = [
    { icon: Battery, label: 'Battery Level', value: `${systemData.Battery_Level.toFixed(2)}%`, color: 'text-green-500' },
    { icon: Shield, label: 'Battery Health', value: `${systemData.Battery_Health.toFixed(2)}%`, color: 'text-blue-500' },
    { icon: Wifi, label: 'Signal Strength', value: `${systemData.Signal_Strength.toFixed(2)}%`, color: 'text-purple-500' },
    { icon: Cpu, label: 'CPU & GPU Usage', value: `${systemData.CPU_GPU_Usage.toFixed(2)}%`, color: 'text-orange-500' },
    { icon: Sun, label: 'Solar Panel Efficiency', value: `${systemData.Solar_Panel_Efficiency.toFixed(2)}%`, color: 'text-yellow-500' },
    { icon: Thermometer, label: 'Temperature', value: `${systemData.Temperature.toFixed(2)}°C`, color: 'text-red-500' },
    { icon: HardDrive, label: 'Data Storage Used', value: `${(systemData.Data_Storage_Used * 100).toFixed(2)} MB`, color: 'text-gray-500' },
    { icon: AlertTriangle, label: 'Debris Risk Level', value: systemData.Debris_Risk_Level.toFixed(2), color: 'text-red-700' },
  ];

  return (
    <div className="space-y-6">
      {/* Status Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => (
          <div key={index} className="bg-white rounded-lg shadow-lg p-6 transform hover:scale-105 transition-transform duration-200">
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <stat.icon className={`h-8 w-8 ${stat.color}`} />
                <div className="ml-4">
                  <p className="text-sm text-gray-600">{stat.label}</p>
                  <p className="text-2xl font-semibold">{stat.value}</p>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* 3D Visualization and Telemetry */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-lg font-semibold mb-4">Satellite Orbit Visualization</h3>
          <SatelliteOrbit satelliteData={[{
            orbital_position_x_km: 0,
            orbital_position_y_km: 0,
            orbital_position_z_km: 0
          }]} />
        </div>
        <div>
          <TelemetryGraphs data={[]} />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
