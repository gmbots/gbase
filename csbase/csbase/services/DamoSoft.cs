using System;
using System.Reflection;
using System.Runtime.InteropServices;

namespace csbase.services {
    public class DamoSoft {
        private Type obj = null;
        private object obj_object = null;

        public DamoSoft() {
            obj = Type.GetTypeFromProgID("dm.dmsoft");
            obj_object = Activator.CreateInstance(obj);
        }

        ~DamoSoft() {
            ReleaseObj();
        }


        private void ReleaseObj() {
            if (obj_object != null) {
                Marshal.ReleaseComObject(obj_object);
                obj_object = null;
            }
        }

        public string Ver() {
            object result;
            result = obj.InvokeMember("Ver", BindingFlags.InvokeMethod, null, obj_object, null);
            return result.ToString();
        }
    }
}