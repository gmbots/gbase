using System;
using System.Reflection;
using System.Runtime.InteropServices;

namespace csbase.services
{
    public class Damo
    {
        private Type obj = null;
        private object obj_object = null;

        public Damo()
        {
            obj = Type.GetTypeFromProgID("dm.dmsoft");
            obj_object = Activator.CreateInstance(obj);
        }

        // 调用此接口进行com对象释放
        public void ReleaseObj()
        {
            if (obj_object != null)
            {
                Marshal.ReleaseComObject(obj_object);
                obj_object = null;
            }
        }

        ~Damo()
        {
            ReleaseObj();
        }

        public string Ver()
        {
            object result;
            result = obj.InvokeMember("Ver", BindingFlags.InvokeMethod, null, obj_object, null);
            return result.ToString();
        }
    }
}