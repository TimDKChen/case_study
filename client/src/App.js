import React, { useState, useEffect } from 'react';
import MaterialTable from '@material-table/core';
import { ExportCsv, ExportPdf } from '@material-table/exporters';
import apiFetch from './utils/apiFetch';

function App() {
  const [tableData, setTableData] = useState([{}]);
  const [nextId, setNextId] = useState(1);
  const columns = [
    { title: "ID", field: "id", filtering: false, grouping: false, width: 90, editable: 'never' },
    { title: "Lots", field: "Lots", filterPlaceholder: "filter", grouping: false, width: 510 },
    { title: "Address", field: "Address", grouping: false, width: 210 },
    { title: "Suburb_PostCode", field: "Suburb_PostCode", grouping: false, width: 210 },
    { title: "Suburb", field: "Suburb", width: 180},
    { title: "Street", field: "Street",filterPlaceholder:"filter" },
    { title: "PostCode", field: "PostCode", width: 90 },
  ]

  useEffect(() => {
    const dicToList = (dict) => {
      const list = [];
      for (let key in dict) {
        list.push({ id: parseInt(key), ...dict[key] })
      }
      return list;
    };
    
    const getData = async () => {
      const resp = await apiFetch('GET', 'todo', null, {})
      // console.log(resp);
      const respToList = dicToList(resp);
      const getId = respToList.length > 0 ? respToList[respToList.length - 1].id + 1 : 1;
      setTableData(respToList);
      setNextId(getId);
    }
    getData();
  }, []);

  return (
    <div className="App" style={{ margin: '30px auto', width: 1440 }}>
      <MaterialTable
        columns={columns}
        data={tableData}
        editable={{
          onRowAdd: (newRow) => new Promise((resolve, reject) => {
            console.log('Add:', newRow);
            newRow.id = nextId;
            var tempId = nextId + 1;
            setTableData([...tableData, newRow]);
            setNextId(tempId);         
            apiFetch('POST', 'todo', null, newRow);
            setTimeout(() => resolve(), 500);
          }),
          onRowUpdate: (newRow, oldRow) => new Promise((resolve, reject) => {
            const updatedData = [...tableData];
            updatedData[oldRow.tableData.index] = newRow;
            setTableData(updatedData);
            apiFetch('PUT', 'todo', null, newRow);
            setTimeout(() => resolve(), 500);
          }),
          onRowDelete: (selectedRow) => new Promise((resolve, reject) => {
            const updatedData = [...tableData];
            const delData = updatedData.filter( (row) => row.id !== selectedRow.id);
            // console.log('del:', updatedData)
            // console.log('index:', selectedRow.tableData.id);
            setTableData(delData);
            apiFetch('DELETE', `todo/?id=${selectedRow.id}`, null, {});
            setTimeout(() => resolve(), 1000);

          })
        }}
        options={{
          sorting: true,
          search: true,
          searchFieldAlignment: "right",
          searchAutoFocus: true,
          searchFieldVariant: "standard",
          filtering: true,
          paging: true,
          pageSizeOptions: [6, 12, 24, 48, 100],
          pageSize: 6,
          paginationType: "normal",
          showFirstLastPageButtons: true,
          paginationPosition: "both",
          addRowPosition: "last",
          actionsColumnIndex: -1,
          grouping: true,
          columnsButton: true,
          rowStyle: (data, index) => index % 2 === 0 ? { background: "#f5f5f5" } : null,
          headerStyle: { background: "#f44336",color:"#fff"},
          exportAllData: true,
          exportMenu: [{
            label: 'Export PDF',
            exportFunc: (cols, datas) => ExportPdf(cols, datas, 'Property'),
          }, {
            label: 'Export CSV',
            exportFunc: (cols, datas) => ExportCsv(cols, datas, 'Property')
          }]
        }}
        title="Property List"
        />
    </div>
  );
}

export default App;
